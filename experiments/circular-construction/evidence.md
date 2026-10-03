# Evidence for autonomous circular construction

Checked 30 September 2026. This is a targeted first pass through primary research, institutional reports, engineering bodies and manufacturers. It is not an exhaustive literature review or a code-compliance assessment. Manufacturer demonstrations and conceptual project descriptions are identified below. No source reviewed establishes the full proposed building system.

## Robots and coordinated construction

| Source | Evidence used | Boundary |
|---|---|---|
| [NASA ARMADAS demonstration, January 2024](https://www.nasa.gov/general/robot-team-builds-high-performance-digital-structure-for-nasa/) | Three robots, hundreds of lightweight composite modules, shed-scale ground assembly, a little over 100 operating hours; differentiated transport, placement and fastening roles | Controlled laboratory system; not steel construction productivity or flight deployment |
| [Gregg et al., Ultra-light, strong, and self-reprogrammable mechanical metamaterials, 2024](https://pubmed.ncbi.nlm.nih.gov/38232146/) | Research abstract describes a 256-unit-cell assembly and disassembly/reconfiguration | Abstract-level evidence here; not proof of whole-building recovery |
| [SCALER, 2024 revision, section VI B2](https://arxiv.org/html/2312.04856v2) | Four articulated limbs; loaded vertical trial: 3.4 kg, 0.16 m/min, a 50 mm rail with coarse sandpaper, two repetitions | Prepared surface and small payload; no basis for projecting heavy steel handling or industrial reliability |
| [KAIST MARVEL laboratory page](https://www.dynamicrobot.kaist.ac.kr/marvel) | Magnetic quadruped climbing on ferromagnetic surfaces; laboratory specifications distinguish wall and ceiling performance | Continuous plate contact differs from open-frame grasping; no beam assembly claim |
| [MIT BILL-E paper](https://cba.mit.edu/docs/papers/17.06.scitech.bille.pdf) | Relative positioning and manipulation in a periodic lattice | Supports robot/environment co-design; scaling to occupied steel buildings is an extrapolation |
| [MIT Shady3D project](https://www.csail.mit.edu/node/6473) | Truss-climbing mechanism and planning research | A locomotion/manipulation precedent, not a construction-rate benchmark |
| [GITAI IN1, 2022](https://gitai.tech/2022/08/16/gitai-develops-inchworm-type-robotic-arm/) | Company-reported ground proof of concept using grapple interfaces and tool exchange | Simulated lunar setting; evidence level is a company demonstration |
| [ETH Spatial Timber Assemblies, 2018](https://ethz.ch/en/news-and-events/eth-news/news/2018/03/spatial-timber-assemblies.html) | Coordinated placement of architectural-scale timber members | Workers bolted connections; cite as robotic placement, not end-to-end autonomous assembly |

## Planning and mechanics

| Source | Evidence used | Boundary |
|---|---|---|
| [Huang et al., Robotic additive construction of bar structures, 2021](https://arxiv.org/abs/2105.11438) | Joint sequence/motion planning accounting for stiffness and geometric constraints, with physical bar-assembly examples | Does not supply the proposed climber, steel connection or building load cases |
| [Peters et al., Assembly Order Planning for Modular Structures, 2025](https://ntrs.nasa.gov/citations/20250002467) | Planning for multiple robots traversing the structure they assemble | Its modular environment is deliberately constrained; algorithmic ideas need adaptation |
| [Motion Planning for a Climbing Robot with Stochastic Grasps, 2022](https://arxiv.org/abs/2209.10687) | Planning couples grasp reliability, posture and load feasibility | Relevant method, not qualification of our proposed docking interface |
| [AISC 303-22, section 7.10](https://www.aisc.org/globalassets/aisc/publications/standards/a303-22w.pdf) | Erection support and permanent lateral-system/diaphragm completion are explicit issues | A structural practice reference; neither a complete analysis nor selection of a jurisdiction's applicable requirements |
| [British Steel section product range, 2025 URL](https://www.britishsteel.co.uk/wp-content/uploads/2025/07/british-steel-product-brochure-14012025-compressed-1.pdf) | UB 254 × 146 × 31 has catalog mass 31.1 kg/m | Used only for handling arithmetic; no member sizing or capacity claim |

The proposed gripper wrench model, temporary capture scheme, mixed fleet and event-driven implementation are our engineering deductions. The literature motivates them but does not certify them.

## Reuse and material recovery

| Source | Evidence used | Boundary |
|---|---|---|
| [SCI P449, Design for the Future](https://www.steelconstruction.info/images/0/0d/SCI_P449.pdf) | Designing steel buildings for future adaptability and reuse | Does not establish the recovery yield of the proposed kit |
| [ECCS PROGRESS, Provisions for greater reuse of steel structures](https://www.steelconstruct.com/wp-content/uploads/PROGRESS-D3.1-Design-for-reuse.pdf) | Reuse-oriented detailing, compatible components, accessible separation and documentation | Guidance must be translated into specific qualified connections |
| [SCI and BCSA, Recycling and reuse](https://steelconstruction.info/topics/sustainability/recycling-and-reuse) | Reuse routes and design considerations | Sector guidance; recyclable material is not proof of collected, qualified output |
| [Gîrbacea et al., Delft demountable floor study, 2019](https://research.tudelft.nl/files/110957617/G_rbacea_et_al_2019_ce_papers.pdf) | Full-scale assembly/disassembly experiments with prefabricated floor elements and beams; tolerance management matters | Specific connection system includes injected connections; cannot be relabeled wholly dry or loss-free |
| [RCSC specifications index](https://www.boltcouncil.org/documents.html) | Publishes a 2025 specification as well as earlier editions | Detailed fastener-reuse policy must be checked against the selected fasteners and current applicable specification; endless bolt reuse is not an assumption |
| [CHANCE helical piles](https://www.hubbell.com/chancefoundationsolutions/en/about-us/chance-products/helical-piles) and [geotechnical FAQ](https://www.hubbell.com/chancefoundationsolutions/en/resources/faqs) | Manufacturer describes segmented piles, loading, removability and installation constraints | A conditional foundation candidate, not a solution for arbitrary soil or tall buildings |
| [European Commission JRC steel circularity briefing](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC142660/JRC142660_01.pdf) | Scrap quality and residual chemistry constrain circular steel production | Not a quantified recovery rate for our system |

## Software references

- [Three.js InstancedMesh](https://threejs.org/docs/pages/InstancedMesh.html): repeated-geometry rendering. No mechanics or structural-validation claim.
- [Three.js GLTFLoader](https://threejs.org/docs/pages/GLTFLoader.html): importing glTF assets, including an optional Blender asset workflow.
- [MuJoCo computation](https://mujoco.readthedocs.io/en/stable/computation/index.html): robot dynamics and contact-model capabilities and limitations.
- [OpenSees modeling capabilities](https://opensees.berkeley.edu/OpenSees/user/modellingCapabilities.php): candidate structural elements and geometric transformations. A solver needs a correct model and independent validation.

## Local intellectual grounding

- [Ren's original material direction](../../worldbuilding/archive/004-ren-regenerative-materials.txt), especially paragraphs on public knowledge, assembled steel buildings, reuse and transformation: primary user-authored antecedent.
- [Regenerative material civilization](../../worldbuilding/foundations/regenerative-material-civilization.md): explicitly AI-developed synthesis; material continuity, recovery routes, public interfaces and successive uses.
- [Generative worldmaking](../../worldbuilding/foundations/generative-worldmaking.md): enabling environments and further possibilities, rather than compulsory activity.
- [Automation to shared abundance](../../worldbuilding/foundations/automation-to-shared-abundance.md): technical capacity and shared provision as a causal program, with dependencies.
- [Architecture for a living Earth](../../theories/architecture-for-a-living-earth/README.md): earlier construction lifecycle and distinction between material circulation and ecological outcomes.
- [MAP](../../MAP.md), the correction concerning growth until needs are met: rapid productive capacity is consistent with the values; its direction and consequences matter.

Reading coverage was bounded to these relevant passages and selected sources. Existing sources and unrelated projects were not edited.
