  t+=.02; ctx.strokeStyle=color; ctx.shadowColor=color; ctx.shadowBlur=18*devicePixelRatio; ctx.lineWidth=2*devicePixelRatio;
  ctx.beginPath();
  for(let a=0;a<Math.PI*2+.01;a+=.012){ let r=R*.58; pcs.forEach(p=>r+=(10+p)*Math.sin((p+2)*a+t+p*.4)); const x=cx+r*Math.cos(a), y=cy+r*Math.sin(a); if(a===0)ctx.moveTo(x,y); else ctx.lineTo(x,y); }
  ctx.closePath(); ctx.stroke(); ctx.shadowBlur=0;
  for(let p=0;p<12;p++){
    const a=(p/12)*Math.PI*2-Math.PI/2, x=cx+R*Math.cos(a), y=cy+R*Math.sin(a), active=pcs.includes(p), isTonic=p===tonic&&pcs.length>0;
    if(isTonic){ ctx.strokeStyle='#ffd700'; ctx.lineWidth=2.5*devicePixelRatio; ctx.beginPath(); ctx.arc(x,y,12*devicePixelRatio,0,Math.PI*2); ctx.stroke(); }
    ctx.fillStyle=active?color:'#333'; ctx.beginPath(); ctx.arc(x,y,(active?7:4)*devicePixelRatio,0,Math.PI*2); ctx.fill();
    ctx.fillStyle=active?'#fff':(isTonic?'#ffd700':'#777'); ctx.font=`${12*devicePixelRatio}px monospace`; ctx.fillText(PITCH.at(p),x+14*devicePixelRatio,y+4*devicePixelRatio);
  }
}
function loop(){ const pcs=current?Object.keys(current.pitch_class_histogram).map(Number).sort((a,b)=>a-b):Array.of(); draw(pcs,current?.overlay_state||'VOID'); requestAnimationFrame(loop); }
updateDiscoveryUI(); mapFormula(); loop();
let current = null;
let prevSnapshot = null;
let atomHistory = Array.of();
const discovered = new Set();

const $ = id => document.getElementById(id);
const mod12 = x => ((x % 12) + 12) % 12;
const dist = (a,b) => { const d = Math.abs(a-b)%12; return d>6 ? 12-d : d; };
const groupPi = g => g === 0 ? 0 : mod12(Math.round(((g - 1) * 12) / 18));
const isNum = tok => /^(\d+\.\d+|\d+)$/.test(tok);

function parseFormula(formula){
  const clean = formula.trim();
  if(!clean) throw new Error('Formula cannot be empty.');
  const tokens = clean.match(/(E0|[A-Z][a-z]?|\(|\)|\d+\.\d+|\d+)/g) || Array.of();
  if(tokens.join('') !== clean) throw new Error('Unsupported formula syntax.');
  const stack = Array.of(new Map());
  const add = (map, key, n) => map.set(key, (map.get(key)||0)+n);
  for(let i=0; i<tokens.length; i++){
    const token = tokens.at(i);
    if(token === '('){ stack.push(new Map()); continue; }
    if(token === ')'){
      if(stack.length === 1) throw new Error('Unmatched closing parenthesis.');
      const group = stack.pop();
      let mult = 1;
      if(tokens.at(i+1) && isNum(tokens.at(i+1))) mult = Number(tokens.at(++i));
      group.forEach((count, symbol) => add(stack.at(-1), symbol, count*mult));
      continue;
    }
    if(isNum(token)) throw new Error('Dangling multiplier: '+token);
    if(Z[token] === undefined) throw new Error('Unknown element: '+token);
    let count = 1;
    if(tokens.at(i+1) && isNum(tokens.at(i+1))) count = Number(tokens.at(++i));
    add(stack.at(-1), token, count);
  }
  if(stack.length !== 1) throw new Error('Unmatched opening parenthesis.');
  return Object.fromEntries(stack.at(0));
}

function hasTritone(u){ for(let i=0;i<u.length;i++) for(let j=i+1;j<u.length;j++) if(dist(u.at(i),u.at(j))===6) return true; return false; }
function hasSemitone(u){ for(let i=0;i<u.length;i++) for(let j=i+1;j<u.length;j++) if(dist(u.at(i),u.at(j))===1) return true; return false; }

function classifyState(unique, nodes){
  if(!unique.length) return 'VOID';
  if(nodes.length === 1 && nodes.at(0).element === 'E0') return 'SUBSTRATE_ZERO';
  if(unique.length === 1) return 'SINGLET_SEED';
  if(unique.length >= 4 && hasSemitone(unique)) return 'PLASMA_FLUX';
  if(hasTritone(unique)) return 'PIEZO_TENSION';
  if(unique.includes(7)) return 'GOLD_ANCHOR';
  if(unique.length >= 3 && unique.some(p => Array.of(0,5,8,10).includes(p))) return 'ARMOR_SHIELD';
  return 'SHADOW_PHASE';
}

function evaluateModalField(normH){
  const normVal = Math.hypot(...normH);
  let best = { score:-1, tonic:0, mode:MODES.at(0), match:0, cModal:0, fource:0 };
  for(let t=0; t<12; t++){
    for(const m of MODES){
      const tplSet = new Set(m.intervals.map(d => mod12(t + d)));
      const tVec = Array(12).fill(0);
      m.intervals.forEach(d => tVec[mod12(t+d)] = 1.0);
      tVec[t] = 2.0; tVec[mod12(t+m.fifth)] += 0.5; tVec[mod12(t+m.char)] += 0.6; tVec[mod12(t+m.third)] += 0.3;
      const normT = Math.hypot(...tVec);
      const dot = normH.reduce((acc, v, idx) => acc + v * tVec.at(idx), 0);
      const cosSim = (normVal > 0 && normT > 0) ? dot / (normVal * normT) : 0;
      const offMass = normH.reduce((acc, v, idx) => acc + (tplSet.has(idx) ? 0 : v), 0);
      const match = Math.max(0, cosSim - 0.5 * offMass);
      const hRoot = normH.at(t), hFifth = normH.at(mod12(t+m.fifth)), hThird = normH.at(mod12(t+m.third)), hChar = normH.at(mod12(t+m.char));
      const cModal = Math.min(1.0,(0.5*hRoot+0.3*hFifth+0.2*hThird)*2.0) * (1.0-offMass) * Math.min(1.0,0.25+1.5*hChar);
      let m2 = 0, tri = 0;
      for(let i=0;i<12;i++) for(let j=i+1;j<12;j++){ const iv=mod12(j-i); if(iv===1||iv===11) m2+=normH.at(i)*normH.at(j); else if(iv===6) tri+=normH.at(i)*normH.at(j); }
      const fource = (hRoot * (hChar + 0.15*hFifth)) / (0.05 + offMass + m2 + tri);
      const score = match + 0.05 * Math.tanh(fource);
      if(score > best.score) best = { score, tonic:t, mode:m, match, cModal, fource };
    }
  }
  return best;
}
function buildSignature(formula, mappingMode='group'){
  const composition = parseFormula(formula);
  const nodes = Object.entries(composition).sort((a,b)=>Z[a.at(0)]-Z[b.at(0)]).map(([symbol,count]) => {
    const atomicNumber = Z[symbol], grp = GRP[symbol], pc = mappingMode === 'group' ? groupPi(grp) : mod12(atomicNumber);
    return { element:symbol, atomic_number:atomicNumber, group:grp, count, pitch_class:pc, pitch_name:PITCH.at(pc), octave_band:atomicNumber===0?0:Math.floor((atomicNumber-1)/12)+1 };
  });
  const rawHist = Array(12).fill(0); nodes.forEach(n => rawHist[n.pitch_class] += n.count);
  const totalW = rawHist.reduce((a,b)=>a+b, 0), normH = totalW > 0 ? rawHist.map(x=>x/totalW) : rawHist;
  const histogram = {}; nodes.forEach(n => histogram[n.pitch_class] = (histogram[n.pitch_class]||0) + n.count);
  const unique = Object.keys(histogram).map(Number).sort((a,b)=>a-b);
  const modal = evaluateModalField(normH);
  const st = classifyState(unique, nodes);
  return {
    formula:formula.trim(), composition, mapping_mode:mappingMode, nodes, pitch_class_histogram:histogram, overlay_state:st,
    modal_field:{ optimal_tonic:modal.tonic, optimal_tonic_name:PITCH.at(modal.tonic), optimal_mode:modal.mode.name, field_type:modal.mode.field, fource_lock:Number(modal.fource.toFixed(4)), c_modal:Number(modal.cModal.toFixed(4)) }
  };
}

function updateDiscoveryUI(){
  const box = $('discoveryBadges');
  box.innerHTML = `<span class="badge unlocked">Discovered: ${discovered.size} / ${STATE_CATALOG.length}</span>` +
    STATE_CATALOG.map(s => `<span class="badge ${discovered.has(s.id)?'unlocked':''}" style="border-color:${discovered.has(s.id)?s.color:'#2a2a2a'}">${s.label}</span>`).join('');
}

function renderSignature(sig, actionNote=''){
  if(current) prevSnapshot = { state: current.overlay_state, fource: current.modal_field.fource_lock };
  current = sig;
  const pcs = Object.keys(sig.pitch_class_histogram).map(Number).sort((a,b)=>a-b), mf = sig.modal_field;
  const cat = STATE_CATALOG.find(s => s.id === sig.overlay_state);
  if(cat) discovered.add(cat.id);
  updateDiscoveryUI();

  $('selected').textContent = sig.formula;
  $('composition').textContent = sig.nodes.map(n => `${n.element}×${n.count} (Z=${n.atomic_number}, Grp ${n.group} → ${n.pitch_name})`).join(' | ');
  $('modalField').textContent = `${mf.optimal_tonic_name} ${mf.optimal_mode} (${mf.field_type})`;
  $('fourceScore').textContent = `F = ${mf.fource_lock.toFixed(3)} | C = ${mf.c_modal.toFixed(3)}`;
  $('classes').textContent = pcs.map(p=>p+'('+PITCH.at(p)+')').join(', ') || '—';
  $('state').textContent = cat ? cat.label.toUpperCase() : sig.overlay_state;
  $('state').style.color = cat ? cat.color : '#00bfff';
  $('stateExplain').innerHTML = cat
    ? `<strong>Kid View:</strong> ${cat.kid}<br><strong>Engineering Hypothesis (L2):</strong> ${cat.eng}`
    : 'Empty stack — click any element tile below to begin.';

  if(actionNote && prevSnapshot){
    const df = mf.fource_lock - prevSnapshot.fource;
    const arrow = df > 0.001 ? '↑' : df < -0.001 ? '↓' : '→';
    $('deltaBanner').innerHTML = `${actionNote} &nbsp;|&nbsp; State: <strong>${prevSnapshot.state}</strong> → <strong>${sig.overlay_state}</strong> &nbsp;|&nbsp; Fource: ${prevSnapshot.fource.toFixed(3)} → <strong>${mf.fource_lock.toFixed(3)} (${arrow})</strong>`;
  }
  [...document.querySelectorAll('.grid button')].forEach((b,i)=>b.classList.toggle('active', sig.nodes.some(n=>n.atomic_number===i)));
}

function mapFormula(actionNote=''){
  try { renderSignature(buildSignature($('formula').value, $('modeSelect').value), actionNote); $('log').classList.remove('error'); }
  catch(err){ $('log').classList.add('error'); $('log').textContent = 'ERROR:\n- ' + err.message; }
}
function loadFormula(f){ atomHistory = Array.of(); $('formula').value = f; mapFormula(`Loaded preset <strong>${f}</strong>`); }
function resetAll(){
  current=null; prevSnapshot=null; atomHistory=Array.of(); $('formula').value=''; $('selected').textContent='—';
  $('composition').textContent='—'; $('modalField').textContent='—'; $('fourceScore').textContent='—';
  $('classes').textContent='—'; $('state').textContent='VOID'; $('state').style.color='#8a8a8a';
  $('stateExplain').textContent='Stack purged — click any element tile below to start a fresh experiment!';
  $('deltaBanner').textContent='Stack purged. Ready for new atoms.';
  [...document.querySelectorAll('.grid button')].forEach(b=>b.classList.remove('active'));
}

function formulaFromHistory(hist){
  const counts = new Map();
  hist.forEach(sym => counts.set(sym, (counts.get(sym)||0) + 1));
  return Array.from(counts.entries()).map(([s,c]) => c > 1 ? `${s}${c}` : s).join('');
}
function stackElement(sym){
  if(atomHistory.length === 0 && $('formula').value === 'SiO2') $('formula').value = '';
  atomHistory.push(sym);
  $('formula').value = formulaFromHistory(atomHistory);
  mapFormula(`Added <strong>${sym}</strong>`);
  if($('autoChime') && $('autoChime').checked) sonify();
}
function undoLast(){
  if(!atomHistory.length){ resetAll(); return; }
  const removed = atomHistory.pop();
  if(!atomHistory.length){ resetAll(); return; }
  $('formula').value = formulaFromHistory(atomHistory);
  mapFormula(`Removed <strong>${removed}</strong>`);
}

function captureAtlas(){ if(!current) return; const mf=current.modal_field; $('log').classList.remove('error'); $('log').textContent += `\n\n[${new Date().toISOString()}] ${current.formula} (${current.mapping_mode}) → ${current.overlay_state} | ${mf.optimal_tonic_name} ${mf.optimal_mode} [F=${mf.fource_lock}, C=${mf.c_modal}]`; }
function downloadLedger(){ if(!current) return; const blob=new Blob(Array.of(JSON.stringify(current,null,2)),{type:'application/json'}); const a=document.createElement('a'); a.href=URL.createObjectURL(blob); a.download=`hte-ledger-${current.formula}.json`; a.click(); }
function sonify(){
  if(!current) mapFormula();
  if(!current) return;
  const ctx = new (window.AudioContext || window.webkitAudioContext)(), now = ctx.currentTime + 0.05;
  current.nodes.forEach((node, i) => {
    const osc = ctx.createOscillator(), gain = ctx.createGain();
    osc.type = current.overlay_state.includes('PIEZO') ? 'triangle' : current.overlay_state.includes('ARMOR') ? 'square' : 'sine';
    osc.frequency.value = 440 * Math.pow(2, ((60 + node.pitch_class + Math.max(0, node.octave_band-1)*3) - 69) / 12);
    const start = now + i * 0.16, dur = Math.min(0.7, 0.22 + node.count * 0.07);
    gain.gain.setValueAtTime(0.0001, start);
    gain.gain.exponentialRampToValueAtTime(Math.min(0.22, 0.07 + node.count * 0.025), start + 0.03);
    gain.gain.exponentialRampToValueAtTime(0.0001, start + dur);
    osc.connect(gain).connect(ctx.destination); osc.start(start); osc.stop(start + dur + 0.05);
  });
}

const gList = $('glossaryList');
STATE_CATALOG.forEach(s => {
  const div = document.createElement('div');
  div.className = 'g-card';
  div.innerHTML = `<div><strong style="color:${s.color}">${s.label}</strong> — ${s.kid}<br><span style="color:#8a8a8a">${s.eng}</span></div><button onclick="loadFormula('${s.example}')">Try ${s.example}</button>`;
  gList.appendChild(div);
});

const grid=$('grid');
ELEMENTS.forEach(e=>{
  const s=e.at(0), z=e.at(1), grp=e.at(2), b=document.createElement('button');
  b.textContent=s+'\n'+z;
  b.style.borderTopColor = PC_COLORS.at(groupPi(grp));
  b.title = `${s} (Z=${z}, Group ${grp} → ${PITCH.at(groupPi(grp))})`;
  b.onclick=()=>stackElement(s);
  grid.appendChild(b);
});

const c=$('scope'), ctx=c.getContext('2d');
function size(){ c.width=c.clientWidth*devicePixelRatio; c.height=c.clientHeight*devicePixelRatio; }
addEventListener('resize',size); size(); let t=0;
function draw(pcs, st){
  ctx.fillStyle='rgba(0,0,0,.2)'; ctx.fillRect(0,0,c.width,c.height);
  const cx=c.width/2, cy=c.height/2, R=Math.min(c.width,c.height)*.33, tonic=current?current.modal_field.optimal_tonic:-1;
  const cat = STATE_CATALOG.find(s => s.id === st);
  const color = cat ? cat.color : '#00bfff';
  ctx.shadowBlur=0; ctx.strokeStyle='#151515'; ctx.lineWidth=1*devicePixelRatio;
  for(let i=0;i<12;i++){ const a=(i/12)*Math.PI*2-Math.PI/2; ctx.beginPath(); ctx.moveTo(cx,cy); ctx.lineTo(cx+R*Math.cos(a),cy+R*Math.sin(a)); ctx.stroke(); }
  ctx.beginPath(); ctx.arc(cx,cy,R,0,Math.PI*2); ctx.stroke();
  t+=.02; ctx.strokeStyle=color; ctx.shadowColor=color; ctx.shadowBlur=18*devicePixelRatio; ctx.lineWidth=2*devicePixelRatio;
  ctx.beginPath();
  for(let a=0;a<Math.PI*2+.01;a+=.012){ let r=R*.58; pcs.forEach(p=>r+=(10+p)*Math.sin((p+2)*a+t+p*.4)); const x=cx+r*Math.cos(a), y=cy+r*Math.sin(a); if(a===0)ctx.moveTo(x,y); else ctx.lineTo(x,y); }
  ctx.closePath(); ctx.stroke(); ctx.shadowBlur=0;
  for(let p=0;p<12;p++){
    const a=(p/12)*Math.PI*2-Math.PI/2, x=cx+R*Math.cos(a), y=cy+R*Math.sin(a), active=pcs.includes(p), isTonic=p===tonic&&pcs.length>0;
    if(isTonic){ ctx.strokeStyle='#ffd700'; ctx.lineWidth=2.5*devicePixelRatio; ctx.beginPath(); ctx.arc(x,y,12*devicePixelRatio,0,Math.PI*2); ctx.stroke(); }
    ctx.fillStyle=active?color:'#333'; ctx.beginPath(); ctx.arc(x,y,(active?7:4)*devicePixelRatio,0,Math.PI*2); ctx.fill();
    ctx.fillStyle=active?'#fff':(isTonic?'#ffd700':'#777'); ctx.font=`${12*devicePixelRatio}px monospace`; ctx.fillText(PITCH.at(p),x+14*devicePixelRatio,y+4*devicePixelRatio);
  }
}
function loop(){ const pcs=current?Object.keys(current.pitch_class_histogram).map(Number).sort((a,b)=>a-b):Array.of(); draw(pcs,current?.overlay_state||'VOID'); requestAnimationFrame(loop); }
updateDiscoveryUI(); mapFormula(); loop();
