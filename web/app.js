const RAW_EL = "E0:0:0:0:0,H:1:1:1:2.2,He:2:18:2:0,Li:3:1:1:0.98,Be:4:2:2:1.57,B:5:13:3:2.04,C:6:14:4:2.55,N:7:15:5:3.04,O:8:16:6:3.44,F:9:17:7:3.98,Ne:10:18:8:0,Na:11:1:1:0.93,Mg:12:2:2:1.31,Al:13:13:3:1.61,Si:14:14:4:1.9,P:15:15:5:2.19,S:16:16:6:2.58,Cl:17:17:7:3.16,Ar:18:18:8:0,K:19:1:1:0.82,Ca:20:2:2:1,Sc:21:3:3:1.36,Ti:22:4:4:1.54,V:23:5:5:1.63,Cr:24:6:6:1.66,Mn:25:7:7:1.55,Fe:26:8:8:1.83,Co:27:9:9:1.88,Ni:28:10:10:1.91,Cu:29:11:11:1.9,Zn:30:12:2:1.65,Ga:31:13:3:1.81,Ge:32:14:4:2.01,As:33:15:5:2.18,Se:34:16:6:2.55,Br:35:17:7:2.96,Kr:36:18:8:3,Rb:37:1:1:0.82,Sr:38:2:2:0.95,Y:39:3:3:1.22,Zr:40:4:4:1.33,Nb:41:5:5:1.6,Mo:42:6:6:2.16,Tc:43:7:7:1.9,Ru:44:8:8:2.2,Rh:45:9:9:2.28,Pd:46:10:10:2.2,Ag:47:11:11:1.93,Cd:48:12:2:1.69,In:49:13:3:1.78,Sn:50:14:4:1.96,Sb:51:15:5:2.05,Te:52:16:6:2.1,I:53:17:7:2.66,Xe:54:18:8:2.6,Cs:55:1:1:0.79,Ba:56:2:2:0.89,La:57:3:3:1.1,Ce:58:3:4:1.12,Pr:59:3:3:1.13,Nd:60:3:3:1.14,Pm:61:3:3:1.13,Sm:62:3:3:1.17,Eu:63:3:2:1.2,Gd:64:3:3:1.2,Tb:65:3:3:1.1,Dy:66:3:3:1.22,Ho:67:3:3:1.23,Er:68:3:3:1.24,Tm:69:3:3:1.25,Yb:70:3:2:1.1,Lu:71:3:3:1.27,Hf:72:4:4:1.3,Ta:73:5:5:1.5,W:74:6:6:2.36,Re:75:7:7:1.9,Os:76:8:8:2.2,Ir:77:9:9:2.2,Pt:78:10:10:2.28,Au:79:11:11:2.54,Hg:80:12:2:2,Tl:81:13:3:1.62,Pb:82:14:4:2.33,Bi:83:15:5:2.02,Po:84:16:6:2,At:85:17:7:2.2,Rn:86:18:8:2.2,Fr:87:1:1:0.7,Ra:88:2:2:0.9,Ac:89:3:3:1.1,Th:90:3:4:1.3,Pa:91:3:5:1.5,U:92:3:6:1.38,Np:93:3:5:1.36,Pu:94:3:4:1.28,Am:95:3:3:1.13,Cm:96:3:3:1.28,Bk:97:3:3:1.3,Cf:98:3:3:1.3,Es:99:3:3:1.3,Fm:100:3:3:1.3,Md:101:3:3:1.3,No:102:3:2:1.3,Lr:103:3:3:1.3,Rf:104:4:4:1.3,Db:105:5:5:1.5,Sg:106:6:6:1.9,Bh:107:7:7:1.9,Hs:108:8:8:2,Mt:109:9:9:2,Ds:110:10:10:2,Rg:111:11:11:2.2,Cn:112:12:2:2,Nh:113:13:3:1.8,Fl:114:14:4:2,Mc:115:15:5:1.9,Lv:116:16:6:2,Ts:117:17:7:2.2,Og:118:18:8:2.2";
const ELEMENTS = RAW_EL.split(",").map(s => { const p = s.split(":"); return Array.of(p.at(0), Number(p.at(1)), Number(p.at(2)), Number(p.at(3)), Number(p.at(4))); });
const Z = Object.fromEntries(ELEMENTS.map(e => Array.of(e.at(0), e.at(1))));
const Z_TO_SYM = Object.fromEntries(ELEMENTS.map(e => Array.of(e.at(1), e.at(0))));
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
  { id:'SINGLET_SEED', label:'Origin / Singlet', color:'#00bfff', example:'H', kid:'Origin Seed — first note of matter before constraint.', eng:'Single pitch-class occupancy; Origin Carrier seed awaiting boundary or bonding relation.' },
  { id:'GOLD_ANCHOR', label:'Gold Anchor', color:'#ffd700', example:'SiO2', kid:'The Rock-Solid Bridge — locked by a strong musical fifth.', eng:'Fifth-anchored harmonic lock; coherent energy/proton transfer or high-symmetry stability.' },
  { id:'PIEZO_TENSION', label:'Piezo Tension', color:'#7cff00', example:'BaTiO3', kid:'The Squeeze-and-Spark Spring — opposite poles pulling tight.', eng:'Contains a 6-semitone tritone axis; polar stress-to-charge or lattice expansion coupling.' },
  { id:'ARMOR_SHIELD', label:'Armor Shield', color:'#ff3b3b', example:'Fe2O3', kid:'The Heavy Fortress Wall — dense boundary shield.', eng:'Subdominant mass clustering; boundary strength (negative when embrittled by interstitial H).' },
  { id:'SHADOW_PHASE', label:'Shadow Phase', color:'#a020f0', example:'GaAs', kid:'The Hidden Twin — stored, trapped, or interstitial phase.', eng:'Interstitial/hydride storage or metastable band-gap switching hidden inside a host lattice.' },
  { id:'PLASMA_FLUX', label:'Plasma Flux', color:'#ff8c00', example:'YBa2Cu3O7', kid:'The Lightning Cloud — super-excited ionized flux.', eng:'High-entropy multi-mode excitation; ionized plasma seed or superionic transport.' }
);
const CANONICAL_DOSSIERS = {
  H: {
    entry_id:'MATLAS-E001-HYDROGEN', status:'canonical draft', name:'Hydrogen',
    cls:'element / gas / plasma-forming carrier / hydride former / isotope platform',
    role:'Origin Node / carrier seed / Fifth-Ladder root',
    isotopes:'1H (protium), 2H (deuterium), 3H (tritium) — all share Z=1 and p(H)=1.',
    states:[
      'Origin: very high — Z=1, first pitch-class root and lattice seed.',
      'Gold: conditional — active in fuel cells, PEM proton transfer, and redox pathways.',
      'Shadow: high — stored, trapped, or absorbed as interstitial hydrides.',
      'Plasma: very high — simplest ionized plasma and fusion seed.',
      'Armor: low / negative at interfaces — weakens metal grain boundaries via embrittlement.',
      'Piezo: indirect — converts pressure/proton transport stress inside host lattices.',
      'Fifth Ladder: canonical root — H → O → P → Ti → Cu → Kr.'
    ],
    iface:['Adsorbs onto surfaces & dissociates from H2 into atomic H','Diffuses rapidly into metals & occupies interstitial sites','Forms metal hydrides & weakens grain boundaries','Participates in proton conduction & alters local electronic structure'],
    fails:['Hydrogen Embrittlement (reduces tensile strength, ductility & fracture toughness)','Leakage & Permeation through seals due to tiny molecular radius','Flammability / Ignition Risk in air (~500°C autoignition)','Cryogenic Risk (boil-off & thermal contraction near -252.9°C)'],
    visible:'Smallest element, light diatomic gas (H2), simple 1s1 structure.',
    hidden:'Embrittlement, seal permeation, storage difficulty, plasma potential, protonic transport, isotope divergence.',
    lock:'Hydrogen = Origin Carrier: the first HTE note, the smallest material actor, and the most boundary-sensitive seed of energy, storage, plasma, and lattice interaction.'
  }
};

const BOUNDARY_PROFILES = {
  free_bulk: { label:'Free Bulk', stateOverride:null, risk:'Low bulk interface stress; watch gas diffusivity / leakage on light carriers.', remainder:'Visible gas/bulk mass; minimal grain-boundary constraint.' },
  metal_host: { label:'Metal Host / Hydride', stateOverride:'SHADOW_PHASE', risk:'HIGH EMBRITTLEMENT RISK: Interstitial H weakens metal grain boundaries & ductility.', remainder:'Hidden interstitial lattice loading & crack-growth remainder.' },
  ceramic_matrix: { label:'Ceramic / Proton Matrix', stateOverride:'GOLD_ANCHOR', risk:'Thermal expansion mismatch & interface permeation at high temperature.', remainder:'Protonic transport channels & entropy redirection across dielectric walls.' },
  cryo_pressure: { label:'Cryo / High-Pressure', stateOverride:'SHADOW_PHASE', risk:'Cryogenic contraction, boil-off pressure rise & seal permeation hazard.', remainder:'High-density confined phase under extreme thermal/pressure constraint.' },
  plasma_excited: { label:'Plasma Excitation', stateOverride:'PLASMA_FLUX', risk:'Thermal wall load, ionization instability & confinement boundary erosion.', remainder:'Ionized collective plasma state exceeding neutral molecular bounds.' }
};
let current = null, prevSnapshot = null, atomHistory = Array.of();
let pinnedElement = null, activeDossierSym = 'H';
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

function classifyState(unique, nodes, boundary){
  if(!unique.length) return 'VOID';
  if(nodes.length === 1 && nodes.at(0).element === 'E0') return 'SUBSTRATE_ZERO';
  const bp = BOUNDARY_PROFILES[boundary];
  if(bp && bp.stateOverride && boundary !== 'free_bulk') return bp.stateOverride;
  if(unique.length === 1) return 'SINGLET_SEED';
  if(unique.length >= 4 && hasSemitone(unique)) return 'PLASMA_FLUX';
  if(hasTritone(unique)) return 'PIEZO_TENSION';
  if(unique.includes(7)) return 'GOLD_ANCHOR';
  if(unique.length >= 3 && unique.some(p => Array.of(0,5,8,10).includes(p))) return 'ARMOR_SHIELD';
  return 'SHADOW_PHASE';
}
function computeCHTE(nodes){
  const pcs = nodes.flatMap(n => Array(Math.max(1, Math.round(n.count))).fill(n.pitch_class));
  if(pcs.length < 2) return 1.0;
  const W = { 0:1.0, 7:0.85, 5:0.75, 4:0.6, 3:0.55, 8:0.5, 9:0.5, 2:0.25, 10:0.25, 6:-0.5, 1:-0.6, 11:-0.6 };
  let sum = 0, pairs = 0;
  for(let i=0;i<pcs.length;i++) for(let j=i+1;j<pcs.length;j++){ sum += W[mod12(pcs.at(j)-pcs.at(i))] || 0; pairs++; }
  return pairs > 0 ? Number((sum / pairs).toFixed(3)) : 1.0;
}

function fifthLadder(rootZ){
  if(!rootZ || rootZ < 1) return 'E0 Substrate';
  const chain = Array.of();
  for(let n=0; n<6; n++){ const zStep = rootZ + 7*n; if(Z_TO_SYM[zStep]) chain.push(Z_TO_SYM[zStep]); }
  return chain.join(' → ');
}

function getElementDossier(sym){
  const z = Z[sym] ?? 0, grp = GRP[sym] ?? 0, val = VAL[sym] ?? 0, chi = CHI[sym] ?? 0;
  const pRaw = mod12(z), pGrp = groupPi(grp), oct = z === 0 ? 0 : Math.floor((z - 1) / 12) + 1;
  const ladder = fifthLadder(z);
  if(CANONICAL_DOSSIERS[sym]) return { ...CANONICAL_DOSSIERS[sym], sym, z, grp, val, chi, pRaw, pGrp, oct, ladder };
  return {
    entry_id:`MATLAS-E${String(z).padStart(3,'0')}-${sym.toUpperCase()}`, status:'auto_derived_v1', name:sym, sym, z, grp, val, chi, pRaw, pGrp, oct, ladder,
    cls:`element / group-${grp} carrier (χ=${chi.toFixed(2)}, valence=${val})`,
    role: z===0 ? 'Substrate Zero / calibration origin' : `Group-${grp} harmonic actor / Fifth-Ladder step-0 node`,
    isotopes:`Natural & synthetic isotopes of ${sym} share Z=${z} and raw pitch class p(${sym})=${pRaw} (${PITCH.at(pRaw)}).`,
    states:[
      `Origin: ${z<=1?'very high':'low'} — Z=${z}, octave layer ${oct}.`,
      `Gold: ${pGrp===7||pRaw===7?'high — fifth-anchored harmonic lock':'conditional — emerges in coherent transfer lattices'}.`,
      `Shadow: ${grp>=3&&grp<=12?'high — d-block interstitial/hydride host candidate':'conditional — interface or defect trapped'}.`,
      `Plasma: ${grp===1||grp===18?'high — low-ionization or discharge plasma actor':'conditional — high-energy excitation'}.`,
      `Armor: ${grp>=6&&grp<=10?'high — structural transition-metal matrix':'conditional — depends on grain-boundary compatibility'}.`,
      `Piezo: ${chi>=2.5||grp===4||grp===17?'high — polar electronegativity gradient':'indirect — stress coupling in asymmetric hosts'}.`,
      `Fifth Ladder: ${ladder}`
    ],
    iface:[`Forms group-${grp} surface & lattice bonds (Pauling χ=${chi.toFixed(2)})`,`Modulates local electronic density & boundary charge transfer`],
    fails:[`Interface reactivity, thermal mismatch, or defect trapping under extreme pressure/temperature`],
    visible:`Z=${z}, Group ${grp}, Valence=${val}, Pauling χ=${chi.toFixed(2)}, HTE (${pRaw}, ${oct}).`,
    hidden:`Boundary-induced phase shifts, grain-boundary compatibility & catalytic/transport remainder.`,
    lock:`${sym} (Z=${z}) = Group-${grp} HTE node at (${pRaw}, ${oct}) whose full behavior emerges under relational boundary constraints.`
  };
}

function renderElementDossier(sym, force = false){
  if(pinnedElement && !force) return;
  activeDossierSym = sym;
  const d = getElementDossier(sym);
  $('dossierTitle').textContent = d.entry_id;
  $('dossierMeta').innerHTML = `STATUS: <strong style="color:${d.status==='canonical draft'?'#ffd700':'#00bfff'}">${d.status}</strong> | HTE Raw: (${d.pRaw}, ${d.oct}) ${PITCH.at(d.pRaw)} | Group: (${d.pGrp}, ${d.oct}) ${PITCH.at(d.pGrp)}`;
  $('dossierBody').innerHTML = `
    <div class="d-lock">${d.lock}</div>
    <div class="d-card"><h2>1. Core &amp; HTE Role</h2><div><strong>Class:</strong> ${d.cls}<br><strong>HTE Role:</strong> ${d.role}<br><strong>Isotopes:</strong> ${d.isotopes}<br><strong>Diatomic Unison:</strong> C_HTE(${d.sym}${d.z>0?'2':''}) = +1.00 | <strong>Fifth Ladder:</strong> ${d.ladder}</div></div>
    <div class="d-card"><h2>2. 7-State Activation Profile</h2><ul>${d.states.map(s=>`<li>${s}</li>`).join('')}</ul></div>
    <div class="d-card"><h2>3. Interface Behavior &amp; Failure Modes</h2><ul>${d.iface.map(i=>`<li>${i}</li>`).join('')}</ul><div style="margin-top:5px;color:#ff9a9a"><strong>Failure Modes:</strong></div><ul>${d.fails.map(f=>`<li>${f}</li>`).join('')}</ul></div>
    <div class="d-card"><h2>4. Darkness Functional Reading</h2><div><strong>Visible:</strong> ${d.visible}<br><strong>Hidden Remainder:</strong> ${d.hidden}</div></div>
  `;
}

function togglePinDossier(){
  pinnedElement = pinnedElement ? null : activeDossierSym;
  $('pinBtn').textContent = pinnedElement ? `📌 Pinned: ${pinnedElement} (Click to Unpin)` : '📌 Unpinned (Hover Live)';
  $('pinBtn').style.borderColor = pinnedElement ? '#ffd700' : '#2a2a2a';
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

function buildSignature(formula, mappingMode='group', weightMode='stoich', boundary='free_bulk'){
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
  const st = classifyState(unique, nodes, boundary);
  const rootNode = nodes.at(0);

  const deltaChi = chis.length >= 2 ? Number((Math.max(...chis) - Math.min(...chis)).toFixed(2)) : 0;
  const meanChi = totalAtoms > 0 ? Number((chiSum / totalAtoms).toFixed(2)) : 0;
  const valPerAtom = totalAtoms > 0 ? Number((totalVal / totalAtoms).toFixed(2)) : 0;

  return {
    entry_id:`MATLAS-${formula.trim().toUpperCase()}`, status:'canonical_draft', formula:formula.trim(),
    composition, mapping_mode:mappingMode, weight_mode:weightMode, boundary_context:boundary,
    hte_coordinate: rootNode ? Array.of(rootNode.pitch_class, rootNode.octave_band) : Array.of(0,0),
    c_hte_unison: computeCHTE(nodes),
    fifth_ladder: fifthLadder(rootNode ? rootNode.atomic_number : 0),
    nodes, pitch_class_histogram:histogram, overlay_state:st,
    interface_profile: BOUNDARY_PROFILES[boundary] || BOUNDARY_PROFILES.free_bulk,
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
  const mf = sig.modal_field, ph = sig.physical, ip = sig.interface_profile;
  const cat = STATE_CATALOG.find(s => s.id === sig.overlay_state);
  if(cat) discovered.add(cat.id);
  updateDiscoveryUI();

  const bondType = ph.delta_chi >= 1.7 ? 'Ionic' : ph.delta_chi >= 0.4 ? 'Polar Covalent' : 'Covalent / Metallic';
  $('selected').textContent = `${sig.formula} → HTE (${sig.hte_coordinate.join(', ')}) | ${sig.nodes.map(n=>`${n.element}×${n.count}`).join(' ')}`;
  $('fifthLadder').textContent = sig.fifth_ladder;
  $('polarityMetrics').textContent = `Δχ = ${ph.delta_chi.toFixed(2)} (${bondType}) | Mean χ = ${ph.mean_chi.toFixed(2)} | Val = ${ph.val_per_atom.toFixed(2)}`;
  $('modalField').textContent = `${mf.optimal_tonic_name} ${mf.optimal_mode} (${mf.field_type})`;
  $('fourceScore').textContent = `C_HTE = ${sig.c_hte_unison >= 0 ? '+' : ''}${sig.c_hte_unison.toFixed(2)} | F = ${mf.fource_lock.toFixed(3)} | C_mod = ${mf.c_modal.toFixed(3)}`;
  $('interfaceRisk').textContent = ip.risk;
  $('state').textContent = cat ? cat.label.toUpperCase() : sig.overlay_state;
  $('state').style.color = cat ? cat.color : '#00bfff';
  $('stateExplain').innerHTML = cat
    ? `<strong>Kid View:</strong> ${cat.kid}<br><strong>Engineering Hypothesis (L2):</strong> ${cat.eng}<br><strong>Darkness Remainder:</strong> ${ip.remainder}`
    : 'Empty stack — click any element tile below to begin.';

  if(actionNote && prevSnapshot){
    const df = mf.fource_lock - prevSnapshot.fource;
    const arrow = df > 0.001 ? '↑' : df < -0.001 ? '↓' : '→';
    $('deltaBanner').innerHTML = `${actionNote} &nbsp;|&nbsp; State: <strong>${prevSnapshot.state}</strong> → <strong>${sig.overlay_state}</strong> &nbsp;|&nbsp; C_HTE: <strong>${sig.c_hte_unison.toFixed(2)}</strong> &nbsp;|&nbsp; Fource: <strong>${mf.fource_lock.toFixed(3)} (${arrow})</strong>`;
  }
  [...document.querySelectorAll('.grid button')].forEach((b,i)=>b.classList.toggle('active', sig.nodes.some(n=>n.atomic_number===i)));
}
function mapFormula(actionNote=''){
  try { renderSignature(buildSignature($('formula').value, $('modeSelect').value, $('weightSelect').value, $('boundarySelect').value), actionNote); $('log').classList.remove('error'); }
  catch(err){ $('log').classList.add('error'); $('log').textContent = 'ERROR:\n- ' + err.message; }
}
function loadFormula(f){ atomHistory = Array.of(); $('formula').value = f; mapFormula(`Loaded preset <strong>${f}</strong>`); }
function resetAll(){
  current=null; prevSnapshot=null; atomHistory=Array.of(); $('formula').value=''; $('selected').textContent='—';
  $('fifthLadder').textContent='—'; $('polarityMetrics').textContent='—'; $('modalField').textContent='—';
  $('fourceScore').textContent='—'; $('interfaceRisk').textContent='—'; $('state').textContent='VOID'; $('state').style.color='#8a8a8a';
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
  if(atomHistory.length === 0 && ($('formula').value === 'H2' || $('formula').value === 'SiO2')) $('formula').value = '';
  atomHistory.push(sym);
  const stacked = formulaFromHistory(atomHistory);
  $('formula').value = stacked;
  if($('dopeBase')){ $('dopeBase').value = stacked; $('dopeSlider').value = 0; $('dopeVal').textContent = '0.00'; drawDopingCurve(0); }
  renderElementDossier(sym, true);
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

function captureAtlas(){ if(!current) return; const mf=current.modal_field; $('log').classList.remove('error'); $('log').textContent += `\n\n[${new Date().toISOString()}] ${current.entry_id} (${current.boundary_context}) → ${current.overlay_state} | C_HTE=${current.c_hte_unison} | Ladder: ${current.fifth_ladder} | ${mf.optimal_tonic_name} ${mf.optimal_mode} [F=${mf.fource_lock}]`; }
function downloadLedger(){ if(!current) return; const blob=new Blob(Array.of(JSON.stringify({ ...current, active_element_dossier: getElementDossier(activeDossierSym) },null,2)),{type:'application/json'}); const a=document.createElement('a'); a.href=URL.createObjectURL(blob); a.download=`${current.entry_id.toLowerCase()}.json`; a.click(); }
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
  if(CANONICAL_DOSSIERS[s]) b.classList.add('has-canonical');
  b.onmouseenter=()=>renderElementDossier(s, false);
  b.onclick=()=>stackElement(s);
  grid.appendChild(b);
});

function buildDopedFormula(base, el, xVal){
  const x = Number(xVal);
  if(x <= 0.001) return base;
  const rx = new RegExp(`(${el})(?![a-z])(\\d*\\.?\\d*)`);
  const m = base.match(rx);
  if(m){ const prev = m.at(2) ? Number(m.at(2)) : 1; return base.replace(rx, `${el}${Number((prev + x).toFixed(2))}`); }
  return `${base}${el}${Number(x.toFixed(2))}`;
}

function drawDopingCurve(activeX = Number($('dopeSlider')?.value || 0.9)){
  const dc = $('dopingChart');
  if(!dc) return;
  dc.width = dc.clientWidth * devicePixelRatio; dc.height = dc.clientHeight * devicePixelRatio;
  const dctx = dc.getContext('2d'), w = dc.width, h = dc.height;
  dctx.clearRect(0, 0, w, h);
  const base = ($('dopeBase')?.value || 'YBa2Cu3O6').trim(), el = ($('dopeEl')?.value || 'O').trim();
  const mode = $('modeSelect').value, weight = $('weightSelect').value, boundary = $('boundarySelect').value, pts = Array.of();
  for(let i = 0; i <= 40; i++){
    const x = i * 0.05;
    try { const sig = buildSignature(buildDopedFormula(base, el, x), mode, weight, boundary); pts.push({ x, f: sig.modal_field.fource_lock }); }
    catch(e) { return; }
  }
  const maxF = Math.max(0.5, ...pts.map(p => p.f));
  dctx.strokeStyle = '#00bfff'; dctx.lineWidth = 2 * devicePixelRatio; dctx.beginPath();
  pts.forEach((p, idx) => {
    const px = (p.x / 2.0) * (w - 20) + 10, py = h - 10 - (p.f / maxF) * (h - 22);
    if(idx === 0) dctx.moveTo(px, py); else dctx.lineTo(px, py);
  });
  dctx.stroke();
  const curPt = pts.reduce((a, b) => Math.abs(b.x - activeX) < Math.abs(a.x - activeX) ? b : a);
  dctx.fillStyle = '#ffd700'; dctx.beginPath();
  dctx.arc((curPt.x / 2.0) * (w - 20) + 10, h - 10 - (curPt.f / maxF) * (h - 22), 4.5 * devicePixelRatio, 0, Math.PI * 2);
  dctx.fill();
  dctx.fillStyle = '#8a8a8a'; dctx.font = `${10 * devicePixelRatio}px monospace`;
  dctx.fillText(`Fource Lock Curve (${base} + x·${el}) | Peak F=${maxF.toFixed(2)}`, 10, 12 * devicePixelRatio);
}

function applyDoping(val){
  const x = Number(val); $('dopeVal').textContent = x.toFixed(2);
  const base = ($('dopeBase')?.value || 'YBa2Cu3O6').trim(), el = ($('dopeEl')?.value || 'O').trim();
  atomHistory = Array.of(); $('formula').value = buildDopedFormula(base, el, x);
  mapFormula(`Doped <strong>${base} + ${x.toFixed(2)} ${el}</strong>`); drawDopingCurve(x);
}
function loadDopingPreset(base, el, x){ $('dopeBase').value = base; $('dopeEl').value = el; $('dopeSlider').value = x; applyDoping(x); }

const c=$('scope'), ctx=c.getContext('2d');
function size(){ c.width=c.clientWidth*devicePixelRatio; c.height=c.clientHeight*devicePixelRatio; }
addEventListener('resize',size); size(); let t=0;
function draw(pcs, st){
  ctx.fillStyle='rgba(0,0,0,.2)'; ctx.fillRect(0,0,c.width,c.height);
  const cx=c.width/2, cy=c.height/2, R=Math.min(c.width,c.height)*.33, tonic=current?current.modal_field.optimal_tonic:-1;
  const cat = STATE_CATALOG.find(s => s.id === st), color = cat ? cat.color : '#00bfff';
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
renderElementDossier('H', true); updateDiscoveryUI(); mapFormula(); drawDopingCurve(); loop();
