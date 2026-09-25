# Automation already helps produce the means of automation

Evidence note · 2026-09-07 · AI-authored research and interpretation for Ren's worldbuilding project.

**The industrial foundation is already substantial.** Automated equipment manufactures robots, machine tools, motors, and controllers. Autonomous vehicles move industrial material flows. Humanoids have performed useful tasks in operating factories, and research systems have assembled large structures from irregular materials. These are concrete starting points for a programme of expanding autonomous production.

The six observations below come from the organizations operating or developing the systems. They establish reported deployments and demonstrations, with different scopes. They are not an independent performance audit. The selected public sources do not establish a factory that autonomously reproduces its complete supply network, nor that today's AI can reliably automate every remaining task. The distinction identifies the engineering programme rather than removing its foundation.

## Six observations

### 1. ABB uses automation to manufacture robots

**Status: opened production facility; operator's account.** On 2 December 2022, ABB opened its Shanghai robotics factory. Its account describes modular, digitally connected production cells supplied by autonomous mobile robots. AI-enabled robotic systems perform screwdriving, assembly, and material handling in the production of new robots. [ABB, factory opening](https://new.abb.com/news/detail/97670/abb-opens-state-of-the-art-robotics-mega-factory-in-shanghai).

**What this supports:** part of the production system already makes equipment that can automate further production. This physical feedback is more concrete than an analogy to software copying itself.

**Boundary:** ABB's description of a fully automated factory does not document autonomous mining, semiconductor fabrication, factory construction, maintenance, or commissioning of a duplicate facility. It describes automation within an existing industrial supply system.

### 2. FANUC automates production of the industrial components underneath robots

**Status: operating factory network; undated company page inspected 7 September 2026.** FANUC describes automated factories producing CNCs, servo motors and amplifiers, robots, and machine tools. Its Mibu operations connect robotized processes with automatic transport, from parts machining through assembly and testing. Tsukuba machines, paints, and assembles parts for robots and machining centres, and produces robot controllers. Headquarters operations include extended periods of unmanned machining. [FANUC, factories](https://www.fanuc.co.jp/en/profile/production/).

**What this supports:** recursive productive expansion concerns a network of complementary machines. Its technical base extends into motion control, machining, and the production of further production equipment.

**Boundary:** the page does not quantify external inputs, intervention hours, or autonomous replacement of every machine. A highly automated component network remains different from a self-sufficient industrial organism.

### 3. BMW's Figure pilot did useful production work over months

**Status: completed factory pilot; manufacturer's report dated 9 March 2026.** BMW reports that Figure 02 supported production of more than 30,000 X3 vehicles during ten months in 2025. It retrieved and positioned sheet-metal parts for welding, moving over 90,000 components during approximately 1,250 operating hours. The integration required changes including additional partitions and improved 5G coverage. [BMW, humanoid production account](https://www.bmwgroup.com/en/news/general/2026/humanoid-robot-in-leipzig.html).

**What this supports:** embodied AI has progressed beyond isolated performances into repeated useful work in a running manufacturing environment. Human-shaped machines can complement existing specialized automation.

**Boundary:** assisting those vehicles means performing a particular process step, not building whole cars. The reported totals do not establish an intervention-free operating rate, general competence across all factory work, or total labour replacement.

**Subsequent development:** BMW's 25 June 2026 announcement describes the next Figure 03 project: sorting components into sequencing trolleys for onward automated transport. Its prospective language establishes an announced next application, not a completed deployment record at the earlier pilot's scale. [BMW, Figure 03 project](https://www.press.bmwgroup.com/canada/article/detail/T0458794EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en).

### 4. Autonomous mining logistics already operate as connected infrastructure

**Status: operating network; live company page inspected 7 September 2026.** Rio Tinto reports that approximately 90% of its Pilbara haul-truck fleet is autonomous, with 40 production drills across seven sites. Its AutoHaul heavy-haul railway began operating in 2018. Trucks, trains, plants, and drills are coordinated through its Perth Operations Centre. The haul trucks follow defined GPS routes; drills can be monitored through remote consoles. [Rio Tinto, Western Australia operations](https://www.riotinto.com/operations/anz/western-australia).

**What this supports:** autonomous material handling is already relevant to the scale of industrial civilization. Linking machines through shared operational systems is an established practice.

**Boundary:** centralized supervision remains part of the account. Autonomous haulage and drilling do not by themselves establish autonomous exploration, all extraction processes, equipment repair, refining, or construction of another mine. The figures describe the page at inspection, not a claimed measurement made on that date.

### 5. Large robot fleets are manufactured, deployed, and improved through shared software

**Status: operator-reported deployment milestone.** On 30 June 2025, Amazon announced deployment of its millionth robot, across a network of more than 300 facilities. The same account describes manufacturing robots in the United States with local suppliers and introducing DeepFleet for fleet coordination. It also describes continuing reliability, maintenance, and engineering roles. [Amazon Robotics, million-robot milestone](https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model).

**What this supports:** physical robot replication through factories and software improvement across installed fleets are already practical at large scale. A useful capability can become available in many places without individually inventing it again.

**Boundary:** a million deployed robots is not a million autonomous general workers, nor evidence that warehouses have no human work. The milestone measures cumulative deployment; it should not be silently reinterpreted as a current count of simultaneously operating robots.

### 6. Robotic construction can handle irregular material in the physical world

**Status: research demonstration reported 22 November 2023.** ETH Zurich reports using its HEAP excavator to construct a dry-stone wall six metres high and 65 metres long. The system mapped the site, scanned stones, assessed properties including approximate weight and centre of gravity, and planned placement. The associated research concerns robotic excavation and construction using on-site materials. [ETH Zurich, autonomous wall construction](https://ethz.ch/en/news-and-events/eth-news/news/2023/11/autonomous-excavator-constructs-a-six-metre-high-dry-stone-wall.html).

**What this supports:** perception, planning, and heavy manipulation can be combined for substantial construction outside a fixed factory cell, including reuse of irregular material.

**Boundary:** this demonstrates a particular construction system and structure. It does not establish autonomous construction of a complete factory with foundations, services, equipment installation, testing, and continuing maintenance.

## The constructive inference

The following is **project reasoning from the observations**, not a conclusion adopted from any company.

An industrial system can direct some output toward producing further productive equipment. When that additional equipment increases the system's ability to produce more equipment, capacity can compound. Robot factories and automated machine-tool/component production already participate in that loop. The new opportunity is to reduce the labour and coordination needed to expand, operate, and reconfigure more of the loop.

The credible unit of expansion is therefore a **productive network**: fabrication, component suppliers, energy, transport, construction, process knowledge, and maintenance. A robot is one participant. Humanoids offer compatibility with some human-built environments; specialized equipment supplies different payloads, precision, speed, or task suitability. Productive expansion need not wait for one machine shape to do everything.

This also changes what can be attempted now. A development programme can choose a useful family of goods, map its process and supply dependencies, automate and standardize successive operations, and use part of its output to expand capacity. Each iteration can document which inputs and interventions still arrive from outside. Expanding the automated share and improving recoverability can be meaningful progress before complete industrial autonomy is achieved.

### When compounding is actually exponential

For a simplified model, let `K` be usable productive capacity. If the rate at which new usable capacity is added remains proportional to `K`, and exceeds proportional retirement, then `dK/dt = gK` for some positive net rate `g`; the model's capacity grows exponentially during that interval. This is a mathematical condition, not a measured growth rate for the systems above.

Keeping `g` positive requires more than producing robot bodies. Energy and component throughput must support the new equipment; sites and logistics must become ready; commissioning must convert equipment into useful production; and maintenance must keep existing capacity functioning. If one necessary upstream process stays fixed, it can cap downstream expansion. None of these sources establishes a complete-network doubling time. No unlimited exponential trajectory is claimed on a finite planet.

The useful insight survives: adding builders can increase the rate at which further building capacity is added. Designing complementary capacity to grow together is a concrete systems problem. For a generative civilization, growth is a means of reaching sufficient and broadly accessible capacity; after that, repair, circulation, and reconfiguration can matter more than adding material stock.

### From productive capacity to freedom from compulsory labour

These observations establish technical resources for reducing human toil. They do not, on their own, decide who receives the output or whether a person must sell labour to gain access to necessities and shared creative means.

The worldbuilding proposal joins two undertakings: build dependable productive systems, and make their provision available as a common foundation. That combination could let people associate freely around gardens, research, games, exploration, and the building of further systems. It treats civilization as an ongoing construction of conditions for good lives, rather than making employment the permanent entry requirement. Where necessary tasks remain, the proposal must account for how they are performed without disguising another group's coercion as everyone's freedom.

## Suggested language for the next worldbook

> We already use automation to produce the tools of automation. Robots manufacture robots; automated systems make machine tools and motion-control components; autonomous vehicles move industrial material flows. This gives us a real industrial starting point for building systems that expand their own productive capacity. The next task is to connect, extend, and make those capabilities dependable enough to sustain a shared material foundation. Our worldbuilding asks what we should create with that foundation, and how everyone can gain the freedom to participate.

This paragraph is an AI-authored synthesis of the six observations and Ren's direction. It should accompany the dated evidence and the distinction between demonstrated operations and the proposed integrated system.

## Scope of this research

This was a bounded primary-source search and reading of ABB, FANUC, BMW, Rio Tinto, Amazon Robotics, and ETH Zurich. It is not an exhaustive survey, comparative economic analysis, current-model AI evaluation, or validation of an autonomous factory design. Semiconductor fabrication, energy expansion, chemical processing, agriculture, general construction, repair autonomy, and the total supply requirements of a proposed system remain unmeasured here. The separate [materials evidence note](2026-09-07-material-circulation.md) addresses circulation and losses. Claims about the sufficiency of current general AI need their own evidence and should not be inferred from the industrial observations alone.
