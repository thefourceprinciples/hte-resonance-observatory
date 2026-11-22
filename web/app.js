const RAW_EL = "E0:0:0,H:1:1,He:2:18,Li:3:1,Be:4:2,B:5:13,C:6:14,N:7:15,O:8:16,F:9:17,Ne:10:18,Na:11:1,Mg:12:2,Al:13:13,Si:14:14,P:15:15,S:16:16,Cl:17:17,Ar:18:18,K:19:1,Ca:20:2,Sc:21:3,Ti:22:4,V:23:5,Cr:24:6,Mn:25:7,Fe:26:8,Co:27:9,Ni:28:10,Cu:29:11,Zn:30:12,Ga:31:13,Ge:32:14,As:33:15,Se:34:16,Br:35:17,Kr:36:18,Rb:37:1,Sr:38:2,Y:39:3,Zr:40:4,Nb:41:5,Mo:42:6,Tc:43:7,Ru:44:8,Rh:45:9,Pd:46:10,Ag:47:11,Cd:48:12,In:49:13,Sn:50:14,Sb:51:15,Te:52:16,I:53:17,Xe:54:18,Cs:55:1,Ba:56:2,La:57:3,Ce:58:3,Pr:59:3,Nd:60:3,Pm:61:3,Sm:62:3,Eu:63:3,Gd:64:3,Tb:65:3,Dy:66:3,Ho:67:3,Er:68:3,Tm:69:3,Yb:70:3,Lu:71:3,Hf:72:4,Ta:73:5,W:74:6,Re:75:7,Os:76:8,Ir:77:9,Pt:78:10,Au:79:11,Hg:80:12,Tl:81:13,Pb:82:14,Bi:83:15,Po:84:16,At:85:17,Rn:86:18,Fr:87:1,Ra:88:2,Ac:89:3,Th:90:3,Pa:91:3,U:92:3,Np:93:3,Pu:94:3,Am:95:3,Cm:96:3,Bk:97:3,Cf:98:3,Es:99:3,Fm:100:3,Md:101:3,No:102:3,Lr:103:3,Rf:104:4,Db:105:5,Sg:106:6,Bh:107:7,Hs:108:8,Mt:109:9,Ds:110:10,Rg:111:11,Cn:112:12,Nh:113:13,Fl:114:14,Mc:115:15,Lv:116:16,Ts:117:17,Og:118:18";
const ELEMENTS = RAW_EL.split(",").map(s => { const p = s.split(":"); return Array.of(p.at(0), Number(p.at(1)), Number(p.at(2))); });
const Z = Object.fromEntries(ELEMENTS.map(e => Array.of(e.at(0), e.at(1))));
const GRP = Object.fromEntries(ELEMENTS.map(e => Array.of(e.at(0), e.at(2))));
const PITCH = Array.of('C','C#','D','Eb','E','F','F#','G','Ab','A','Bb','B');
const MODES = Array.of(
  { name:'Ionian', intervals:Array.of(0,2,4,5,7,9,11), char:11, third:4, fifth:7, field:'Structural Clarity Field' },
  { name:'Dorian', intervals:Array.of(0,2,3,5,7,9,10), char:9, third:3, fifth:7, field:'Restoration Field' },
  { name:'Phrygian', intervals:Array.of(0,1,3,5,7,8,10), char:1, third:3, fifth:7, field:'Boundary / Threshold Field' },
  { name:'Lydian', intervals:Array.of(0,2,4,6,7,9,11), char:6, third:4, fifth:7, field:'Expansion / Levitation Field' },
  { name:'Mixolydian', intervals:Array.of(0,2,4,5,7,9,10), char:10, third:4, fifth:7, field:'Continuity Field' },
  { name:'Aeolian', intervals:Array.of(0,2,3,5,7,8,10), char:8, third:3, fifth:7, field:'Memory / Gravitational Field' },
  { name:'Locrian', intervals:Array.of(0,1,3,5,6,8,10), char:6, third:3, fifth:6, field:'Fracture / Collapse Field' }
);

let current = null;
let startedStack = false;
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

function intervalWalk(u){ return u.length<2 ? Array.of() : u.map((p,i)=>mod12(u.at((i+1)%u.length)-p)); }
function hasTritone(u){ for(let i=0;i<u.length;i++) for(let j=i+1;j<u.length;j++) if(dist(u.at(i),u.at(j))===6) return true; return false; }
function stateOf(u){
  if(!u.length) return 'VOID';
  if(hasTritone(u)) return 'PIEZO_OVERLAY_CANDIDATE';
  if(u.includes(7)) return 'GOLD_OVERLAY_CANDIDATE';
  if(u.length>=3 && u.some(p=>Array.of(0,5,8,10).includes(p))) return 'ARMOR_OVERLAY_CANDIDATE';
  return 'MIXED_OVERLAY';
}
function tagsFor(st, modeName){
  let h = st.includes('GOLD')?'<span class="tag gold">Gold overlay</span>':st.includes('PIEZO')?'<span class="tag piezo">Piezo overlay</span>':st.includes('ARMOR')?'<span class="tag armor">Armor overlay</span>':'<span class="tag">Mixed</span>';
  return modeName ? h + `<span class="tag shadow">${modeName}</span>` : h;
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
  const weightedChord = nodes.flatMap(n => Array(Math.max(1, Math.round(n.count))).fill(n.pitch_class));
  const rawHist = Array(12).fill(0); nodes.forEach(n => rawHist[n.pitch_class] += n.count);
  const totalW = rawHist.reduce((a,b)=>a+b, 0), normH = totalW > 0 ? rawHist.map(x=>x/totalW) : rawHist;
  const histogram = {}; nodes.forEach(n => histogram[n.pitch_class] = (histogram[n.pitch_class]||0) + n.count);
  const unique = Object.keys(histogram).map(Number).sort((a,b)=>a-b);
  const modal = evaluateModalField(normH);
  const sortedEntries = Object.entries(histogram).sort((a,b)=>b.at(1)-a.at(1));
  return {
    formula:formula.trim(), composition, mapping_mode:mappingMode, nodes, weighted_chord:weightedChord, pitch_class_histogram:histogram,
    interval_walk:intervalWalk(unique), dominant_pitch_class:weightedChord.length?Number(sortedEntries.at(0).at(0)):null, overlay_state:stateOf(unique),
    modal_field:{ optimal_tonic:modal.tonic, optimal_tonic_name:PITCH.at(modal.tonic), optimal_mode:modal.mode.name, field_type:modal.mode.field, fource_lock:Number(modal.fource.toFixed(4)), c_modal:Number(modal.cModal.toFixed(4)) }
  };
}

function renderSignature(sig){
  current = sig;
  const pcs = Object.keys(sig.pitch_class_histogram).map(Number).sort((a,b)=>a-b), mf = sig.modal_field;
  $('selected').textContent = sig.formula;
  $('composition').textContent = Object.entries(sig.composition).map(([s,c])=>s+':'+c).join(' ');
  $('modalField').textContent = `${mf.optimal_tonic_name} ${mf.optimal_mode} (${mf.field_type})`;
  $('fourceScore').textContent = `F = ${mf.fource_lock.toFixed(3)} | C = ${mf.c_modal.toFixed(3)}`;
  $('classes').textContent = pcs.map(p=>p+'('+PITCH.at(p)+')').join(' ') || '—';
  $('chord').textContent = '[' + sig.weighted_chord.join(', ') + ']';
  $('walk').textContent = sig.interval_walk.length ? sig.interval_walk.join('-') : '—';
  $('state').textContent = sig.overlay_state;
  $('tags').innerHTML = tagsFor(sig.overlay_state, mf.optimal_mode);
  [...document.querySelectorAll('.grid button')].forEach((b,i)=>b.classList.toggle('active', sig.nodes.some(n=>n.atomic_number===i)));
}

function mapFormula(){
  try { renderSignature(buildSignature($('formula').value, $('modeSelect').value)); $('log').classList.remove('error'); }
  catch(err){ $('log').classList.add('error'); $('log').textContent = 'ERROR:\n- ' + err.message; }
}
function loadFormula(f){ $('formula').value = f; startedStack = false; mapFormula(); }
function resetAll(){
  current=null; startedStack=false; $('formula').value=''; $('selected').textContent='—'; $('composition').textContent='—';
  $('modalField').textContent='—'; $('fourceScore').textContent='—'; $('classes').textContent='—'; $('chord').textContent='—';
  $('walk').textContent='—'; $('state').textContent='VOID'; $('tags').innerHTML=''; $('log').classList.remove('error');
  $('log').textContent='MATERIALS ATLAS LOG:\n- No entries yet.';
  [...document.querySelectorAll('.grid button')].forEach(b=>b.classList.remove('active'));
}
function stackElement(sym){
  let cur = startedStack ? $('formula').value.trim() : '';
  startedStack = true;
  const rx = new RegExp(`(${sym})(\\d*)$`);
  const m = cur.match(rx);
  if(m){
    const nextCnt = m.at(2) ? Number(m.at(2)) + 1 : 2;
    cur = cur.replace(rx, `${sym}${nextCnt}`);
  } else {
    cur += sym;
  }
  $('formula').value = cur;
  mapFormula();
}
function captureAtlas(){ if(!current) return; const mf=current.modal_field; $('log').classList.remove('error'); $('log').textContent += `\n\n[${new Date().toISOString()}] ${current.formula} (${current.mapping_mode}) → ${mf.optimal_tonic_name} ${mf.optimal_mode} | F=${mf.fource_lock} | ${current.overlay_state}`; }
function downloadLedger(){ if(!current) return; const blob=new Blob(Array.of(JSON.stringify(current,null,2)),{type:'application/json'}); const a=document.createElement('a'); a.href=URL.createObjectURL(blob); a.download=`hte-ledger-${current.formula}.json`; a.click(); }
function sonify(){
  if(!current) mapFormula();
  if(!current) return;
  const ctx = new (window.AudioContext || window.webkitAudioContext)(), now = ctx.currentTime + 0.05;
  current.nodes.forEach((node, i) => {
    const osc = ctx.createOscillator(), gain = ctx.createGain();
    osc.type = current.overlay_state.includes('PIEZO') ? 'triangle' : current.overlay_state.includes('ARMOR') ? 'square' : 'sine';
    osc.frequency.value = 440 * Math.pow(2, ((60 + node.pitch_class + Math.max(0, node.octave_band-1)*3) - 69) / 12);
    const start = now + i * 0.18, dur = Math.min(0.75, 0.22 + node.count * 0.08);
    gain.gain.setValueAtTime(0.0001, start);
    gain.gain.exponentialRampToValueAtTime(Math.min(0.22, 0.07 + node.count * 0.025), start + 0.03);
    gain.gain.exponentialRampToValueAtTime(0.0001, start + dur);
    osc.connect(gain).connect(ctx.destination); osc.start(start); osc.stop(start + dur + 0.05);
  });
}

const grid=$('grid');
ELEMENTS.forEach(e=>{ const s=e.at(0), z=e.at(1), b=document.createElement('button'); b.textContent=s+'\n'+z; b.onclick=()=>stackElement(s); grid.appendChild(b); });
const c=$('scope'), ctx=c.getContext('2d');
function size(){ c.width=c.clientWidth*devicePixelRatio; c.height=c.clientHeight*devicePixelRatio; }
addEventListener('resize',size); size(); let t=0;
function draw(pcs, st){
  ctx.fillStyle='rgba(0,0,0,.2)'; ctx.fillRect(0,0,c.width,c.height);
  const cx=c.width/2, cy=c.height/2, R=Math.min(c.width,c.height)*.33, tonic=current?current.modal_field.optimal_tonic:-1;
  const color=st.includes('PIEZO')?'#7cff00':st.includes('GOLD')?'#ffd700':st.includes('ARMOR')?'#ff3b3b':'#00bfff';
  ctx.shadowBlur=0; ctx.strokeStyle='#151515'; ctx.lineWidth=1*devicePixelRatio;
  for(let i=0;i<12;i++){ const a=(i/12)*Math.PI*2-Math.PI/2; ctx.beginPath(); ctx.moveTo(cx,cy); ctx.lineTo(cx+R*Math.cos(a),cy+R*Math.sin(a)); ctx.stroke(); }
  ctx.beginPath(); ctx.arc(cx,cy,R,0,Math.PI*2); ctx.stroke();
  t+=.02; ctx.strokeStyle=color; ctx.shadowColor=color; ctx.shadowBlur=18*devicePixelRatio; ctx.lineWidth=2*devicePixelRatio;
  ctx.beginPath();
  for(let a=0;a<Math.PI*2+.01;a+=.012){ let r=R*.58; pcs.forEach(p=>r+=(10+p)*Math.sin((p+2)*a+t+p*.4)); const x=cx+r*Math.cos(a), y=cy+r*Math.sin(a); if(a===0)ctx.moveTo(x,y); else ctx.lineTo(x,y); }
  ctx.closePath(); ctx.stroke(); ctx.shadowBlur=0;
  for(let p=0;p<12;p++){
    const a=(p/12)*Math.PI*2-Math.PI/2, x=cx+R*Math.cos(a), y=cy+R*Math.sin(a), active=pcs.includes(p), isTonic=p===tonic&&pcs.length>0;
    ctx.fillStyle=isTonic?'#ffd700':(active?color:'#333'); ctx.beginPath(); ctx.arc(x,y,(isTonic?9:active?7:4)*devicePixelRatio,0,Math.PI*2); ctx.fill();
    ctx.fillStyle=isTonic?'#ffd700':(active?'#fff':'#777'); ctx.font=`${12*devicePixelRatio}px monospace`; ctx.fillText(PITCH.at(p),x+10*devicePixelRatio,y+4*devicePixelRatio);
  }
}
function loop(){ const pcs=current?Object.keys(current.pitch_class_histogram).map(Number).sort((a,b)=>a-b):Array.of(); draw(pcs,current?.overlay_state||'VOID'); requestAnimationFrame(loop); }
mapFormula(); loop();
