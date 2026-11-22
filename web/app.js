const RAW_EL = "E0:0:0:0:0,H:1:1:1:2.2,He:2:18:2:0,Li:3:1:1:0.98,Be:4:2:2:1.57,B:5:13:3:2.04,C:6:14:4:2.55,N:7:15:5:3.04,O:8:16:6:3.44,F:9:17:7:3.98,Ne:10:18:8:0,Na:11:1:1:0.93,Mg:12:2:2:1.31,Al:13:13:3:1.61,Si:14:14:4:1.9,P:15:15:5:2.19,S:16:16:6:2.58,Cl:17:17:7:3.16,Ar:18:18:8:0,K:19:1:1:0.82,Ca:20:2:2:1,Sc:21:3:3:1.36,Ti:22:4:4:1.54,V:23:5:5:1.63,Cr:24:6:6:1.66,Mn:25:7:7:1.55,Fe:26:8:8:1.83,Co:27:9:9:1.88,Ni:28:10:10:1.91,Cu:29:11:11:1.9,Zn:30:12:2:1.65,Ga:31:13:3:1.81,Ge:32:14:4:2.01,As:33:15:5:2.18,Se:34:16:6:2.55,Br:35:17:7:2.96,Kr:36:18:8:3,Rb:37:1:1:0.82,Sr:38:2:2:0.95,Y:39:3:3:1.22,Zr:40:4:4:1.33,Nb:41:5:5:1.6,Mo:42:6:6:2.16,Tc:43:7:7:1.9,Ru:44:8:8:2.2,Rh:45:9:9:2.28,Pd:46:10:10:2.2,Ag:47:11:11:1.93,Cd:48:12:2:1.69,In:49:13:3:1.78,Sn:50:14:4:1.96,Sb:51:15:5:2.05,Te:52:16:6:2.1,I:53:17:7:2.66,Xe:54:18:8:2.6,Cs:55:1:1:0.79,Ba:56:2:2:0.89,La:57:3:3:1.1,Ce:58:3:4:1.12,Pr:59:3:3:1.13,Nd:60:3:3:1.14,Pm:61:3:3:1.13,Sm:62:3:3:1.17,Eu:63:3:2:1.2,Gd:64:3:3:1.2,Tb:65:3:3:1.1,Dy:66:3:3:1.22,Ho:67:3:3:1.23,Er:68:3:3:1.24,Tm:69:3:3:1.25,Yb:70:3:2:1.1,Lu:71:3:3:1.27,Hf:72:4:4:1.3,Ta:73:5:5:1.5,W:74:6:6:2.36,Re:75:7:7:1.9,Os:76:8:8:2.2,Ir:77:9:9:2.2,Pt:78:10:10:2.28,Au:79:11:11:2.54,Hg:80:12:2:2,Tl:81:13:3:1.62,Pb:82:14:4:2.33,Bi:83:15:5:2.02,Po:84:16:6:2,At:85:17:7:2.2,Rn:86:18:8:2.2,Fr:87:1:1:0.7,Ra:88:2:2:0.9,Ac:89:3:3:1.1,Th:90:3:4:1.3,Pa:91:3:5:1.5,U:92:3:6:1.38,Np:93:3:5:1.36,Pu:94:3:4:1.28,Am:95:3:3:1.13,Cm:96:3:3:1.28,Bk:97:3:3:1.3,Cf:98:3:3:1.3,Es:99:3:3:1.3,Fm:100:3:3:1.3,Md:101:3:3:1.3,No:102:3:2:1.3,Lr:103:3:3:1.3,Rf:104:4:4:1.3,Db:105:5:5:1.5,Sg:106:6:6:1.9,Bh:107:7:7:1.9,Hs:108:8:8:2,Mt:109:9:9:2,Ds:110:10:10:2,Rg:111:11:11:2.2,Cn:112:12:2:2,Nh:113:13:3:1.8,Fl:114:14:4:2,Mc:115:15:5:1.9,Lv:116:16:6:2,Ts:117:17:7:2.2,Og:118:18:8:2.2";
const ELEMENTS = RAW_EL.split(",").map(s => { const p = s.split(":"); return Array.of(p.at(0), Number(p.at(1)), Number(p.at(2)), Number(p.at(3)), Number(p.at(4))); });
const Z = Object.fromEntries(ELEMENTS.map(e => Array.of(e.at(0), e.at(1))));
const GRP = Object.fromEntries(ELEMENTS.map(e => Array.of(e.at(0), e.at(2))));
const VAL = Object.fromEntries(ELEMENTS.map(e => Array.of(e.at(0), e.at(3))));
const CHI = Object.fromEntries(ELEMENTS.map(e => Array.of(e.at(0), e.at(4))));
const PITCH = Array.of('C','C#','D','Eb','E','F','F#','G','Ab','A','Bb','B');
const PC_COLORS = Array.of('#00bfff','#ff55aa','#7cff00','#a020f0','#ffd700','#ff6b6b','#00ffcc','#ffaa00','#b388ff','#69f0ae','#ff80ab','#40c4ff');

const MODES = Array.of(
  { name:'Ionian', intervals:Array.of(0,2,4,5,7,9,11), char:11, third:4, fifth:7, field:'Structural Clarity Field' },
  { name:'Dorian', intervals:Array.of(0,2,3,5,7,9,10), char:9, third:3, fifth:7, field:'Restoration Field' },
  { name:'Phrygian', intervals:Array.of(0,1,3,5,7,8,10), char:1, third:3, fifth:7, field:'Boundary / Threshold Field' },
  { name:'Lydian', intervals:Array.of(0,2,4,6,7,9,11), char:6, third:4, fifth:7, field:'Expansion / Levitation Field' },
  { name:'Mixolydian', intervals:Array.of(0,2,4,5,7,9,10), char:10, third:4, fifth:7, field:'Continuity Field' },
  { name:'Aeolian', intervals:Array.of(0,2,3,5,7,8,10), char:8, third:3, fifth:7, field:'Memory / Gravitational Field' },
  { name:'Locrian', intervals:Array.of(0,1,3,5,6,8,10), char:6, third:3, fifth:6, field:'Fracture / Collapse Field' }
);

const STATE_CATALOG = Array.of(
  { id:'SUBSTRATE_ZERO', label:'Substrate Zero', color:'#ffffff', example:'E0', kid:'The Quiet Blank Canvas — zero-atom background field.', eng:'Null-reference substrate (Z=0, π=0, ω=0) for baseline calibration.' },
  { id:'SINGLET_SEED', label:'Singlet Seed', color:'#00bfff', example:'H', kid:'One Lone Atom Looking for a Friend — unbonded single note.', eng:'Single pitch-class occupancy; high Locrian tritone pull awaiting a bonding partner.' },
  { id:'GOLD_ANCHOR', label:'Gold Anchor', color:'#ffd700', example:'SiO2', kid:'The Rock-Solid Bridge — locked by a strong musical fifth.', eng:'Anchored on pitch class 7 (G); candidate for high-symmetry bridging and low-friction stability.' },
  { id:'PIEZO_TENSION', label:'Piezo Tension', color:'#7cff00', example:'BaTiO3', kid:'The Squeeze-and-Spark Spring — opposite poles pulling tight.', eng:'Contains a 6-semitone tritone axis; candidate for polar asymmetry and electromechanical stress coupling.' },
  { id:'ARMOR_SHIELD', label:'Armor Shield', color:'#ff3b3b', example:'Fe2O3', kid:'The Heavy Fortress Wall — dense multi-atom shield.', eng:'3+ pitch classes anchored on {C, F, Ab, Bb}; candidate for mass damping and structural load absorption.' },
  { id:'SHADOW_PHASE', label:'Shadow Phase', color:'#a020f0', example:'GaAs', kid:'The Hidden Twin — dark minor/phrygian phase shifter.', eng:'Tritone-free dark cluster without dominant fifth; candidate for metastable switching or band-gap hysteresis.' },
  { id:'PLASMA_FLUX', label:'Plasma Flux', color:'#ff8c00', example:'YBa2Cu3O7', kid:'The Lightning Cloud — super-excited multi-note energy.', eng:'4+ pitch classes with adjacent semitone (m2) friction; candidate for high-entropy transport or catalytic flux.' }
);

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

function buildSignature(formula, mappingMode='group', weightMode='stoich'){
  const composition = parseFormula(formula);
  const chis = Array.of();
  let totalAtoms = 0, totalVal = 0, chiSum = 0;

  const nodes = Object.entries(composition).sort((a,b)=>Z[a.at(0)]-Z[b.at(0)]).map(([symbol,count]) => {
    const atomicNumber = Z[symbol], grp = GRP[symbol], val = VAL[symbol], chi = CHI[symbol];
    const pc = mappingMode === 'group' ? groupPi(grp) : mod12(atomicNumber);
    if(chi > 0){ chis.push(chi); chiSum += count * chi; }
    totalAtoms += count; totalVal += count * val;
    return { element:symbol, atomic_number:atomicNumber, group:grp, valence:val, chi, count, pitch_class:pc, pitch_name:PITCH.at(pc), octave_band:atomicNumber===0?0:Math.floor((atomicNumber-1)/12)+1 };
  });

  const rawHist = Array(12).fill(0);
  nodes.forEach(n => {
    const w = weightMode === 'electronegativity' ? n.count * (n.chi > 0 ? n.chi : 0.1)
            : weightMode === 'valence' ? n.count * (n.valence > 0 ? n.valence : 0.1)
            : n.count;
    rawHist[n.pitch_class] += w;
  });
  const totalW = rawHist.reduce((a,b)=>a+b, 0), normH = totalW > 0 ? rawHist.map(x=>x/totalW) : rawHist;
  const histogram = {}; nodes.forEach(n => histogram[n.pitch_class] = (histogram[n.pitch_class]||0) + n.count);
  const unique = Object.keys(histogram).map(Number).sort((a,b)=>a-b);
  const modal = evaluateModalField(normH);
  const st = classifyState(unique, nodes);

  const deltaChi = chis.length >= 2 ? Number((Math.max(...chis) - Math.min(...chis)).toFixed(2)) : 0;
  const meanChi = totalAtoms > 0 ? Number((chiSum / totalAtoms).toFixed(2)) : 0;
  const valPerAtom = totalAtoms > 0 ? Number((totalVal / totalAtoms).toFixed(2)) : 0;

  return {
    formula:formula.trim(), composition, mapping_mode:mappingMode, weight_mode:weightMode, nodes, pitch_class_histogram:histogram, overlay_state:st,
    physical:{ delta_chi:deltaChi, mean_chi:meanChi, val_per_atom:valPerAtom },
    modal_field:{ optimal_tonic:modal.tonic, optimal_tonic_name:PITCH.at(modal.tonic), optimal_mode:modal.mode.name, field_type:modal.mode.field, fource_lock:Number(modal.fource.toFixed(4)), c_modal:Number(modal.cModal.toFixed(4)) }
  };
}

function updateDiscoveryUI(){
  const box = $('discoveryBadges');
  box.innerHTML = `<span class="badge unlocked">Discovered: ${discovered.size} / ${STATE_CATALOG.length}</span>` +
    STATE_CATALOG.map(s => `<span class="badge ${discovered.has(s.id)?'unlocked':''}" style="border-color:${discovered.has(s.id)?s.color:'#2a2a2a'}">${s.label}</span>`).join('');
}

function renderSignature(sig, actionNote=''){
  if(current) prevSnapshot = { state: current.overlay_state, fource: current.modal_field.fource_lock, dchi: current.physical.delta_chi };
  current = sig;
  const pcs = Object.keys(sig.pitch_class_histogram).map(Number).sort((a,b)=>a-b), mf = sig.modal_field, ph = sig.physical;
  const cat = STATE_CATALOG.find(s => s.id === sig.overlay_state);
  if(cat) discovered.add(cat.id);
  updateDiscoveryUI();

  const bondType = ph.delta_chi >= 1.7 ? 'Ionic' : ph.delta_chi >= 0.4 ? 'Polar Covalent' : 'Covalent / Metallic';
  $('selected').textContent = sig.formula;
  $('composition').textContent = sig.nodes.map(n => `${n.element}×${n.count} (Grp ${n.group}, χ=${n.chi} → ${n.pitch_name})`).join(' | ');
  $('polarityMetrics').textContent = `Δχ = ${ph.delta_chi.toFixed(2)} (${bondType}) | Mean χ = ${ph.mean_chi.toFixed(2)} | Val/atom = ${ph.val_per_atom.toFixed(2)}`;
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
    $('deltaBanner').innerHTML = `${actionNote} &nbsp;|&nbsp; State: <strong>${prevSnapshot.state}</strong> → <strong>${sig.overlay_state}</strong> &nbsp;|&nbsp; Δχ: ${prevSnapshot.dchi.toFixed(2)} → <strong>${ph.delta_chi.toFixed(2)}</strong> &nbsp;|&nbsp; Fource: <strong>${mf.fource_lock.toFixed(3)} (${arrow})</strong>`;
  }
  [...document.querySelectorAll('.grid button')].forEach((b,i)=>b.classList.toggle('active', sig.nodes.some(n=>n.atomic_number===i)));
}

function mapFormula(actionNote=''){
  try { renderSignature(buildSignature($('formula').value, $('modeSelect').value, $('weightSelect').value), actionNote); $('log').classList.remove('error'); }
  catch(err){ $('log').classList.add('error'); $('log').textContent = 'ERROR:\n- ' + err.message; }
}
function loadFormula(f){ atomHistory = Array.of(); $('formula').value = f; mapFormula(`Loaded preset <strong>${f}</strong>`); }
function resetAll(){
  current=null; prevSnapshot=null; atomHistory=Array.of(); $('formula').value=''; $('selected').textContent='—';
  $('composition').textContent='—'; $('polarityMetrics').textContent='—'; $('modalField').textContent='—';
  $('fourceScore').textContent='—'; $('classes').textContent='—'; $('state').textContent='VOID'; $('state').style.color='#8a8a8a';
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

function captureAtlas(){ if(!current) return; const mf=current.modal_field, ph=current.physical; $('log').classList.remove('error'); $('log').textContent += `\n\n[${new Date().toISOString()}] ${current.formula} (${current.mapping_mode}/${current.weight_mode}) → ${current.overlay_state} | Δχ=${ph.delta_chi}, Val=${ph.val_per_atom} | ${mf.optimal_tonic_name} ${mf.optimal_mode} [F=${mf.fource_lock}, C=${mf.c_modal}]`; }
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
function mapFormula(actionNote=''){
  try { renderSignature(buildSignature($('formula').value, $('modeSelect').value, $('weightSelect').value), actionNote); $('log').classList.remove('error'); }
  catch(err){ $('log').classList.add('error'); $('log').textContent = 'ERROR:\n- ' + err.message; }
}
function loadFormula(f){ atomHistory = Array.of(); $('formula').value = f; mapFormula(`Loaded preset <strong>${f}</strong>`); }
function resetAll(){
  current=null; prevSnapshot=null; atomHistory=Array.of(); $('formula').value=''; $('selected').textContent='—';
  $('composition').textContent='—'; $('polarityMetrics').textContent='—'; $('modalField').textContent='—';
  $('fourceScore').textContent='—'; $('classes').textContent='—'; $('state').textContent='VOID'; $('state').style.color='#8a8a8a';
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

function captureAtlas(){ if(!current) return; const mf=current.modal_field, ph=current.physical; $('log').classList.remove('error'); $('log').textContent += `\n\n[${new Date().toISOString()}] ${current.formula} (${current.mapping_mode}/${current.weight_mode}) → ${current.overlay_state} | Δχ=${ph.delta_chi}, Val=${ph.val_per_atom} | ${mf.optimal_tonic_name} ${mf.optimal_mode} [F=${mf.fource_lock}, C=${mf.c_modal}]`; }
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
  const s=e.at(0), z=e.at(1), grp=e.at(2), val=e.at(3), chi=e.at(4), b=document.createElement('button');
  b.textContent=s+'\n'+z;
  b.style.borderTopColor = PC_COLORS.at(groupPi(grp));
  b.title = `${s} (Z=${z}, Grp ${grp}, Val=${val}, χ=${chi} → ${PITCH.at(groupPi(grp))})`;
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
