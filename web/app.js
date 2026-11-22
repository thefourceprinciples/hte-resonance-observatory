const RAW_EL = "E0:0:0:0:0:0:sub:None,H:1:1:1:2.2:1.008:gas:1H|2H|3H,He:2:18:2:0:4.003:gas:3He|4He,Li:3:1:1:0.98:6.94:solid:6Li|7Li,Be:4:2:2:1.57:9.012:solid:9Be|10Be,B:5:13:3:2.04:10.81:solid:10B|11B,C:6:14:4:2.55:12.011:solid:12C|13C|14C,N:7:15:5:3.04:14.007:gas:14N|15N,O:8:16:6:3.44:15.999:gas:16O|17O|18O,F:9:17:7:3.98:18.998:gas:19F|18F,Ne:10:18:8:0:20.180:gas:20Ne|21Ne|22Ne,Na:11:1:1:0.93:22.990:solid:23Na|22Na|24Na,Mg:12:2:2:1.31:24.305:solid:24Mg|25Mg|26Mg,Al:13:13:3:1.61:26.982:solid:27Al|26Al,Si:14:14:4:1.9:28.085:solid:28Si|29Si|30Si,P:15:15:5:2.19:30.974:solid:31P|32P|33P,S:16:16:6:2.58:32.06:solid:32S|33S|34S|36S,Cl:17:17:7:3.16:35.45:gas:35Cl|37Cl|36Cl,Ar:18:18:8:0:39.948:gas:40Ar|36Ar|38Ar,K:19:1:1:0.82:39.098:solid:39K|41K|40K,Ca:20:2:2:1:40.078:solid:40Ca|44Ca|42Ca|48Ca,Sc:21:3:3:1.36:44.956:solid:45Sc|46Sc,Ti:22:4:4:1.54:47.867:solid:48Ti|46Ti|47Ti|49Ti|50Ti,V:23:5:5:1.63:50.942:solid:51V|50V,Cr:24:6:6:1.66:51.996:solid:52Cr|53Cr|50Cr|54Cr,Mn:25:7:7:1.55:54.938:solid:55Mn|53Mn|54Mn,Fe:26:8:8:1.83:55.845:solid:56Fe|54Fe|57Fe|58Fe,Co:27:9:9:1.88:58.933:solid:59Co|60Co|57Co,Ni:28:10:10:1.91:58.693:solid:58Ni|60Ni|62Ni|61Ni,Cu:29:11:11:1.9:63.546:solid:63Cu|65Cu|64Cu,Zn:30:12:2:1.65:65.38:solid:64Zn|66Zn|68Zn|67Zn,Ga:31:13:3:1.81:69.723:solid:69Ga|71Ga|67Ga,Ge:32:14:4:2.01:72.630:solid:74Ge|72Ge|70Ge|76Ge,As:33:15:5:2.18:74.922:solid:75As|73As,Se:34:16:6:2.55:78.971:solid:80Se|78Se|76Se|82Se,Br:35:17:7:2.96:79.904:liquid:79Br|81Br,Kr:36:18:8:3:83.798:gas:84Kr|86Kr|82Kr|83Kr,Rb:37:1:1:0.82:85.468:solid:85Rb|87Rb,Sr:38:2:2:0.95:87.62:solid:88Sr|86Sr|87Sr|90Sr,Y:39:3:3:1.22:88.906:solid:89Y|90Y,Zr:40:4:4:1.33:91.224:solid:90Zr|94Zr|92Zr|91Zr,Nb:41:5:5:1.6:92.906:solid:93Nb|94Nb,Mo:42:6:6:2.16:95.95:solid:98Mo|96Mo|95Mo|92Mo,Tc:43:7:7:1.9:98:solid:99Tc|97Tc|98Tc,Ru:44:8:8:2.2:101.07:solid:102Ru|104Ru|101Ru|99Ru,Rh:45:9:9:2.28:102.91:solid:103Rh|105Rh,Pd:46:10:10:2.2:106.42:solid:106Pd|108Pd|105Pd|110Pd,Ag:47:11:11:1.93:107.87:solid:107Ag|109Ag,Cd:48:12:2:1.69:112.41:solid:114Cd|112Cd|111Cd|110Cd,In:49:13:3:1.78:114.82:solid:115In|113In,Sn:50:14:4:1.96:118.71:solid:120Sn|118Sn|116Sn|119Sn,Sb:51:15:5:2.05:121.76:solid:121Sb|123Sb,Te:52:16:6:2.1:127.60:solid:130Te|128Te|126Te,I:53:17:7:2.66:126.90:solid:127I|129I|131I,Xe:54:18:8:2.6:131.29:gas:132Xe|129Xe|131Xe|136Xe,Cs:55:1:1:0.79:132.91:solid:133Cs|137Cs,Ba:56:2:2:0.89:137.33:solid:138Ba|137Ba|136Ba|135Ba,La:57:3:3:1.1:138.91:solid:139La|138La,Ce:58:3:4:1.12:140.12:solid:140Ce|142Ce,Pr:59:3:3:1.13:140.91:solid:141Pr,Nd:60:3:3:1.14:144.24:solid:142Nd|144Nd|146Nd|143Nd,Pm:61:3:3:1.13:145:solid:145Pm|147Pm,Sm:62:3:3:1.17:150.36:solid:152Sm|154Sm|147Sm|149Sm,Eu:63:3:2:1.2:151.96:solid:153Eu|151Eu,Gd:64:3:3:1.2:157.25:solid:158Gd|160Gd|156Gd|157Gd,Tb:65:3:3:1.1:158.93:solid:159Tb,Dy:66:3:3:1.22:162.50:solid:164Dy|162Dy|163Dy|161Dy,Ho:67:3:3:1.23:164.93:solid:165Ho,Er:68:3:3:1.24:167.26:solid:166Er|168Er|167Er|170Er,Tm:69:3:3:1.25:168.93:solid:169Tm,Yb:70:3:2:1.1:173.05:solid:174Yb|172Yb|173Yb|171Yb,Lu:71:3:3:1.27:174.97:solid:175Lu|176Lu,Hf:72:4:4:1.3:178.49:solid:180Hf|178Hf|177Hf|179Hf,Ta:73:5:5:1.5:180.95:solid:181Ta|180mTa,W:74:6:6:2.36:183.84:solid:184W|186W|182W|183W,Re:75:7:7:1.9:186.21:solid:187Re|185Re,Os:76:8:8:2.2:190.23:solid:192Os|190Os|189Os|188Os,Ir:77:9:9:2.2:192.22:solid:193Ir|191Ir,Pt:78:10:10:2.28:195.08:solid:195Pt|194Pt|196Pt|198Pt,Au:79:11:11:2.54:196.97:solid:197Au|198Au,Hg:80:12:2:2:200.59:liquid:202Hg|200Hg|199Hg|201Hg,Tl:81:13:3:1.62:204.38:solid:205Tl|203Tl,Pb:82:14:4:2.33:207.2:solid:208Pb|206Pb|207Pb|204Pb,Bi:83:15:5:2.02:208.98:solid:209Bi,Po:84:16:6:2:209:solid:209Po|210Po|208Po,At:85:17:7:2.2:210:solid:210At|211At,Rn:86:18:8:2.2:222:gas:222Rn|220Rn,Fr:87:1:1:0.7:223:solid:223Fr,Ra:88:2:2:0.9:226:solid:226Ra|228Ra,Ac:89:3:3:1.1:227:solid:227Ac,Th:90:3:4:1.3:232.04:solid:232Th|230Th,Pa:91:3:5:1.5:231.04:solid:231Pa,U:92:3:6:1.38:238.03:solid:238U|235U|234U,Np:93:3:5:1.36:237:solid:237Np,Pu:94:3:4:1.28:244:solid:244Pu|239Pu|240Pu|238Pu,Am:95:3:3:1.13:243:solid:243Am|241Am,Cm:96:3:3:1.28:247:solid:247Cm|244Cm|248Cm,Bk:97:3:3:1.3:247:solid:247Bk|249Bk,Cf:98:3:3:1.3:251:solid:251Cf|252Cf|249Cf,Es:99:3:3:1.3:252:solid:252Es|254Es,Fm:100:3:3:1.3:257:solid:257Fm,Md:101:3:3:1.3:258:solid:258Md|260Md,No:102:3:2:1.3:259:solid:259No,Lr:103:3:3:1.3:266:solid:266Lr|262Lr,Rf:104:4:4:1.3:267:synthetic:267Rf|265Rf,Db:105:5:5:1.5:268:synthetic:268Db|270Db,Sg:106:6:6:1.9:269:synthetic:269Sg|271Sg,Bh:107:7:7:1.9:270:synthetic:270Bh|274Bh,Hs:108:8:8:2:277:synthetic:277Hs|270Hs,Mt:109:9:9:2:278:synthetic:278Mt|276Mt,Ds:110:10:10:2:281:synthetic:281Ds|279Ds,Rg:111:11:11:2.2:282:synthetic:282Rg|280Rg,Cn:112:12:2:2:285:synthetic:285Cn|283Cn,Nh:113:13:3:1.8:286:synthetic:286Nh|284Nh,Fl:114:14:4:2:289:synthetic:289Fl|287Fl,Mc:115:15:5:1.9:290:synthetic:290Mc|288Mc,Lv:116:16:6:2:293:synthetic:293Lv|291Lv,Ts:117:17:7:2.2:294:synthetic:294Ts|293Ts,Og:118:18:8:2.2:294:synthetic:294Og";
const ELEMENTS = RAW_EL.split(",").map(s => { const p = s.split(":"); return Array.of(p.at(0), Number(p.at(1)), Number(p.at(2)), Number(p.at(3)), Number(p.at(4)), Number(p.at(5)), p.at(6), p.at(7)); });
const Z = Object.fromEntries(ELEMENTS.map(e => Array.of(e.at(0), e.at(1))));
const Z_TO_SYM = Object.fromEntries(ELEMENTS.map(e => Array.of(e.at(1), e.at(0))));
const GRP = Object.fromEntries(ELEMENTS.map(e => Array.of(e.at(0), e.at(2))));
const VAL = Object.fromEntries(ELEMENTS.map(e => Array.of(e.at(0), e.at(3))));
const CHI = Object.fromEntries(ELEMENTS.map(e => Array.of(e.at(0), e.at(4))));
const MASS = Object.fromEntries(ELEMENTS.map(e => Array.of(e.at(0), e.at(5))));
const PHASE = Object.fromEntries(ELEMENTS.map(e => Array.of(e.at(0), e.at(6))));
const ISOTOPES = Object.fromEntries(ELEMENTS.map(e => Array.of(e.at(0), e.at(7).split("|"))));
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

const BOUNDARY_PROFILES = {
  free_bulk: { label:'Free Bulk', stateOverride:null, risk:'Low bulk interface stress; watch gas diffusivity / leakage on light carriers.', remainder:'Visible gas/bulk mass; minimal grain-boundary constraint.' },
  metal_host: { label:'Metal Host / Hydride', stateOverride:'SHADOW_PHASE', risk:'HIGH EMBRITTLEMENT RISK: Interstitial H weakens metal grain boundaries & ductility.', remainder:'Hidden interstitial lattice loading & crack-growth remainder.' },
  ceramic_matrix: { label:'Ceramic / Proton Matrix', stateOverride:'GOLD_ANCHOR', risk:'Thermal expansion mismatch & interface permeation at high temperature.', remainder:'Protonic transport channels & entropy redirection across dielectric walls.' },
  cryo_pressure: { label:'Cryo / High-Pressure', stateOverride:'SHADOW_PHASE', risk:'Cryogenic contraction, boil-off pressure rise & seal permeation hazard.', remainder:'High-density confined phase under extreme thermal/pressure constraint.' },
  plasma_excited: { label:'Plasma Excitation', stateOverride:'PLASMA_FLUX', risk:'Thermal wall load, ionization instability & confinement boundary erosion.', remainder:'Ionized collective plasma state exceeding neutral molecular bounds.' }
};
const CANONICAL_DOSSIERS = {
  H: {
    entry_id:'MATLAS-E001-HYDROGEN', status:'canonical draft', name:'Hydrogen',
    cls:'element / gas / plasma-forming carrier / hydride former / isotope platform',
    role:'Origin Node / carrier seed / Fifth-Ladder root',
    isoNote:'1H = protium (dominant), 2H = deuterium (fusion-relevant), 3H = tritium (radioactive). All share Z=1 and p(H)=1.',
    chordNote:'Atomic chord {1}; diatomic H2 chord {1, 1} with I(H,H)=0 and C_HTE(H2)=+1.00 (pure unison lock).',
    constraints:'Pressure, temperature, confinement, surface catalysis, metal lattice compatibility, leakage & ignition control.',
    thermal:'Cryogenic liquid below 20.27 K (-252.9°C); high energy per mass, low volumetric density as gas.',
    energy:'High mobility energy carrier; clean oxidation to H2O; proton conductor in PEM fuel cells; fusion feedstock.',
    storage:['1. Compressed gas','2. Cryogenic liquid','3. Metal hydride (Shadow State)','4. Chemical carrier','5. Adsorbent material','6. Geological storage','7. Pipeline distribution'],
    cuc:['H2 gas → fuel / carrier / leakage risk','H+ → proton / acid / conductor participant','H- → hydride / reducer','D → heavy isotope / fusion platform','Plasma H → stellar / ionized state','Metal-H → interstitial storage / embrittlement'],
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
    measure:['Basic: purity, isotope ratio, molecular form, pressure, temperature','Storage: leak rate, permeation rate, adsorption capacity, hysteresis','Compatibility: embrittlement response, crack growth rate, fatigue life','Energy/Interface: reaction enthalpy, proton conductivity, plasma threshold'],
    search:['1. Fifth Ladder materials (H → O → P → Ti → Cu → Kr)','2. Hydride storage systems (Shadow/Armor balance)','3. Proton conductors (H + ceramic/polymer matrices)','4. Embrittlement-resistant alloys & hydrogen-safe barrier coatings','5. Optical/electrical/mechanical H2 sensors'],
    visible:'Smallest element, light diatomic gas (H2), simple 1s1 structure.',
    hidden:'Embrittlement, seal permeation, storage difficulty, plasma potential, protonic transport, isotope divergence.',
    fourcePhrase:'Hydrogen is the first note of matter, but it only becomes a song under constraint.',
    lock:'Hydrogen = Origin Carrier: the first HTE note, the smallest material actor, and the most boundary-sensitive seed of energy, storage, plasma, and lattice interaction.'
  }
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
  const mass = MASS[sym] ?? 0, phase = PHASE[sym] ?? 'solid', isos = ISOTOPES[sym] || Array.of();
  const pRaw = mod12(z), pGrp = groupPi(grp), oct = z === 0 ? 0 : Math.floor((z - 1) / 12) + 1;
  const ladder = fifthLadder(z);
  const base = { sym, z, grp, val, chi, mass, phase, isos, pRaw, pGrp, oct, ladder };
  if(CANONICAL_DOSSIERS[sym]) return { ...base, ...CANONICAL_DOSSIERS[sym] };

  const isGas = phase === 'gas', isSyn = phase === 'synthetic', isMetal = grp >= 1 && grp <= 12 && !isGas;
  return {
    ...base,
    entry_id:`MATLAS-E${String(z).padStart(3,'0')}-${sym.toUpperCase()}`, status:'auto_derived_v1', name:sym,
    cls:`element / ${phase} at 20°C / group-${grp} carrier (χ=${chi.toFixed(2)}, valence=${val})`,
    role: z===0 ? 'Substrate Zero / zero-octave calibration origin' : `Group-${grp} harmonic actor / Fifth-Ladder step-0 node`,
    isoNote: z===0 ? 'Zero-nucleon reference field (no isotopes).' : `Primary isotopes: ${isos.join(', ')}. All share Z=${z} and raw pitch class p(${sym})=${pRaw} (${PITCH.at(pRaw)}); isotopes diverge in neutron mass and nuclear stability only.`,
    chordNote: z===0 ? 'Null substrate chord {0}.' : `Atomic chord {${pRaw}}; diatomic ${sym}2 chord {${pRaw}, ${pRaw}} with I(${sym},${sym})=0 and C_HTE=${1.00.toFixed(2)} (unison lock).`,
    constraints: isGas ? 'Pressure, cryogenic/compressed containment, seal permeation & leak control.' : isSyn ? 'Nuclear half-life, radiation shielding & remote hot-cell containment.' : 'Temperature, surface oxidation, grain-boundary stress & lattice compatibility.',
    thermal: isGas ? 'Cryogenic liquid below boiling point; low volumetric gas density.' : isMetal ? 'Conductive crystalline solid; thermal expansion & creep under high load.' : 'Directional covalent/dielectric thermal transport; watch thermal shock.',
    energy: chi >= 2.5 ? 'High-electronegativity charge acceptor / redox & dielectric actor.' : grp === 1 ? 'High-mobility electron/ion donor (battery & plasma carrier).' : 'Structural, catalytic, or electronic network host.',
    storage: isGas ? ['1. Compressed gas cylinders','2. Cryogenic liquid','3. Adsorbent/clathrate matrix','4. Pipeline distribution'] : isSyn ? ['1. Shielded radiological containment','2. Target foil / isotopic trap'] : ['1. Bulk crystalline ingot / powder','2. Passivated surface / inert atmosphere','3. Alloyed or ceramic host matrix'],
    cuc: z===0 ? ['E0 → unperturbed carrier medium before atomic boundary conditions'] : [`Bulk ${sym} → baseline ${phase} phase`,`Ionized ${sym} → charge-transfer / plasma actor`,`Interface ${sym} → boundary-coupled catalyst or lattice modifier`,`Isotopic ${isos.at(0)||sym} → mass-shifted phonon & nuclear response`],
    states:[
      `Origin: ${z<=1?'very high':'low'} — Z=${z}, octave layer ${oct}.`,
      `Gold: ${pGrp===7||pRaw===7?'high — fifth-anchored harmonic lock':'conditional — emerges in coherent transfer lattices'}.`,
      `Shadow: ${grp>=3&&grp<=12?'high — d-block interstitial/hydride host candidate':'conditional — interface or defect trapped'}.`,
      `Plasma: ${isGas||grp===1?'high — low-ionization or discharge plasma actor':'conditional — high-energy excitation'}.`,
      `Armor: ${isMetal&&grp>=4?'high — structural metallic matrix':'conditional — depends on grain-boundary compatibility'}.`,
      `Piezo: ${chi>=2.5||grp===4||grp===17?'high — polar electronegativity gradient':'indirect — stress coupling in asymmetric hosts'}.`,
      `Fifth Ladder: ${ladder}`
    ],
    iface:[`Forms group-${grp} surface & lattice bonds (Pauling χ=${chi.toFixed(2)})`,`Modulates local electronic density & boundary charge transfer`],
    fails:[`Interface reactivity, thermal mismatch, or defect trapping under extreme pressure/temperature`],
    measure:['Basic: purity, isotope ratio, stoichiometry, pressure, temperature','Compatibility: grain-boundary stability, corrosion/oxidation rate','Interface: surface adsorption energy, diffusion coefficient'],
    search:[`1. Fifth Ladder pathway (${ladder})`,`2. Binary/ternary oxides & hydrides with Δχ contrast`,`3. Boundary-stabilized coatings & alloy hosts`],
    visible:`Z=${z}, Mass=${mass} u, Group ${grp}, Valence=${val}, Pauling χ=${chi.toFixed(2)}, STP=${phase}.`,
    hidden:`Isotope mass divergence (${isos.join('/')}), interface charge transfer & boundary-dependent phase shifts.`,
    fourcePhrase:`${sym} is note ${PITCH.at(pRaw)} in octave ${oct}, revealing its full engineering song only under boundary constraint.`,
    lock:`${sym} (Z=${z}) = Group-${grp} HTE node at (${pRaw}, ${oct}) whose bulk chord shifts under relational boundary constraints.`
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
    <div class="d-card"><h2>1. Core Identity &amp; HTE Signature</h2><div><strong>Class:</strong> ${d.cls}<br><strong>HTE Role:</strong> ${d.role}<br><strong>Atomic Weight / STP:</strong> ${d.mass} u | ${d.phase} at 20°C | Valence: ${d.val} | χ: ${d.chi}<br><strong>Chord &amp; Unison:</strong> ${d.chordNote}<br><strong>Fifth Ladder:</strong> ${d.ladder}</div></div>
    <div class="d-card"><h2>2. Isotopic Identity (Pitch-Invariant)</h2><div>${d.isoNote}</div></div>
    <div class="d-card"><h2>3. Constraint, Thermal &amp; Energy Fields</h2><div><strong>Constraints:</strong> ${d.constraints}<br><strong>Thermal:</strong> ${d.thermal}<br><strong>Energy Role:</strong> ${d.energy}</div></div>
    <div class="d-card"><h2>4. Storage &amp; Containment Modes</h2><ul>${d.storage.map(s=>`<li>${s}</li>`).join('')}</ul></div>
    <div class="d-card"><h2>5. CUC Relational Constraint Map</h2><div><em>"${d.fourcePhrase}"</em></div><ul>${d.cuc.map(c=>`<li>${c}</li>`).join('')}</ul></div>
    <div class="d-card"><h2>6. 7-State Activation Profile</h2><ul>${d.states.map(s=>`<li>${s}</li>`).join('')}</ul></div>
    <div class="d-card"><h2>7. Interface Behavior &amp; Failure Modes</h2><ul>${d.iface.map(i=>`<li>${i}</li>`).join('')}</ul><div style="margin-top:5px;color:#ff9a9a"><strong>Failure Modes:</strong></div><ul>${d.fails.map(f=>`<li>${f}</li>`).join('')}</ul></div>
    <div class="d-card"><h2>8. Darkness Remainder &amp; Measurement Stack</h2><div><strong>Visible:</strong> ${d.visible}<br><strong>Hidden Remainder:</strong> ${d.hidden}</div><ul style="margin-top:4px">${d.measure.map(m=>`<li>${m}</li>`).join('')}</ul></div>
    <div class="d-card"><h2>9. HTE Search Directions</h2><ul>${d.search.map(s=>`<li>${s}</li>`).join('')}</ul></div>
  `;
}

function togglePinDossier(){
  pinnedElement = pinnedElement ? null : activeDossierSym;
  $('pinBtn').textContent = pinnedElement ? `📌 Pinned: ${pinnedElement}` : '📌 Unpinned';
  $('pinBtn').style.borderColor = pinnedElement ? '#ffd700' : '#2a2a2a';
}

function copyDossierMarkdown(){
  const d = getElementDossier(activeDossierSym);
  const md = `# Materials Atlas Entry: ${d.name} (${d.sym})\n**ENTRY ID:** ${d.entry_id} | **STATUS:** ${d.status}\n**CLASS:** ${d.cls}\n**HTE ROLE:** ${d.role}\n\n## Core & Isotopic Identity\n- Z=${d.z}, Mass=${d.mass} u, Group=${d.grp}, Valence=${d.val}, Pauling χ=${d.chi}, STP=${d.phase}\n- ${d.isoNote}\n- HTE Coordinate: Raw (${d.pRaw}, ${d.oct}) ${PITCH.at(d.pRaw)} | Group (${d.pGrp}, ${d.oct}) ${PITCH.at(d.pGrp)}\n- ${d.chordNote}\n- Fifth Ladder: ${d.ladder}\n\n## 7-State Activation\n${d.states.map(s=>'- '+s).join('\n')}\n\n## Interface Behavior & Failure Modes\n${d.iface.map(i=>'- '+i).join('\n')}\n\n**Failure Modes:**\n${d.fails.map(f=>'- '+f).join('\n')}\n\n## Storage & Containment\n${d.storage.map(s=>'- '+s).join('\n')}\n\n## CUC Relational Map & Darkness Reading\n${d.cuc.map(c=>'- '+c).join('\n')}\n- Visible: ${d.visible}\n- Hidden Remainder: ${d.hidden}\n\n## Measurement Stack & Search Directions\n${d.measure.map(m=>'- '+m).join('\n')}\n${d.search.map(s=>'- '+s).join('\n')}\n\n**One-Line Lock:** ${d.lock}`;
  navigator.clipboard.writeText(md).then(() => {
    $('copyMdBtn').textContent = '✅ Copied!';
    setTimeout(() => { $('copyMdBtn').textContent = '📋 Copy .md'; }, 1800);
  });
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
