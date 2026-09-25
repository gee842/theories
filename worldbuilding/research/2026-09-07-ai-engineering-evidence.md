# AI as useful cognitive and physical capacity

Research note · 2026-09-07 · AI-authored synthesis of five primary evidence cases. This is a bounded capability check for the worldbuilding's technical foundation, not an exhaustive review of robotics or an independent audit of the reporting organizations. Publication dates and evaluation scope matter; a later access date does not make an older result a new achievement.

## What the evidence lets us say positively

We already have working methods for connecting learned perception, language, task decomposition, tool use, motor control, feedback, and training. These methods are producing useful action in physical settings and deployed improvements to computing infrastructure. An autonomous system need not be a mysterious new kind of machine: these examples show concrete ways to compose one and improve it through experience.

The constructive implication is substantial. We can pursue broader automation by building, measuring, adapting environments, collecting failures, improving controllers, and connecting services. The examples below make that an empirical engineering and research program. They do not establish that the present generation of AI is sufficient for every physical job, or that every remaining problem is already solved in principle.

## Five primary evidence cases

### 1. Planning, tools, action, and recovery are connected in one physical agent

**Gemini Robotics 1.5.** Announced September 25, 2025; technical-report version examined: November 28, 2025.

The system combines an embodied-reasoning model with a vision-language-action model. The former decomposes tasks, uses external tools, and checks progress; the latter executes robot actions. The report evaluates skill transfer across ALOHA, bi-arm Franka, and Apollo, including tasks whose demonstrations came from another embodiment. Its eight long-horizon tests include retrieving outside information, remembering object arrangements, and recovering from errors. One illustrated recovery switches hands after a bottle slips. [Technical report, sections 2, 3.2–3.3, and 5](https://arxiv.org/html/2510.03342v3).

**Engineering significance:** one can connect semantic understanding to execution and use observed consequences to choose the next action. **Boundary:** these are bounded robot experiments. Some Franka long-horizon tests use additional post-training. The frequently reported near-80% figures are task-progress scores, not evidence of 80% complete autonomy across arbitrary work. [Technical report, section 5 and appendix D](https://arxiv.org/html/2510.03342v3).

### 2. Physical skills can transfer into places absent from training

**Physical Intelligence's π0.5.** Published April 22, 2025.

The researchers combine robot demonstrations across embodiments and environments with web-derived visual-language data, semantic subtask labels, and verbal coaching. A mobile manipulator then performs household tasks in previously unseen homes, including moving dishes, tidying bedrooms, and wiping surfaces. Their ablations show that the different data sources contribute to generalization. In the reported environment-scaling study, training across about 100 environments approaches a comparison policy trained with data from the test environment itself. [Authors' account and linked paper](https://www.pi.website/blog/pi05).

**Engineering significance:** useful behavior need not be programmed separately for every room, object arrangement, or robot. Shared training can make capabilities more reusable. **Boundary:** this is demonstrated transfer of a task repertoire, not unrestricted acquisition of any skill. Reported success is averaged over subtasks; it must not be relabeled as the probability of flawlessly completing an entire home-cleaning job. [Authors' evaluation definitions](https://www.pi.website/blog/pi05).

### 3. Learned robot policies are doing real customer work

**Physical Intelligence, Weave, and Ultra deployment accounts.** Published February 24, 2026.

Weave describes π0.6 folding laundry in live laundromat deployments. Ultra describes robots packing actual customer orders and presents a continuous full-shift recording labeled **96.4% autonomy**. The account describes repeated improvements across model generations, and explains that human intervention both resolves failures and generates data for later training. These are reports by the model developer and its deploying partners, accompanied by deployment footage, rather than independent fleet audits. [The Physical Intelligence Layer](https://www.pi.website/blog/partner).

**Engineering significance:** adaptable policies have crossed into useful operational tasks; deployment experience can feed capability improvement. **Boundary:** the advertised autonomy figure is not a universal success rate or an estimate of jobs eliminated. Remote specialists remain involved. The same article explicitly describes important open research problems in making a reusable physical-intelligence layer generally accessible. [Deployment account](https://www.pi.website/blog/partner).

### 4. Robot skills can be learned in simulation and transferred to hardware

**DextrAH-RGB, NVIDIA and UC Berkeley authors.** First submitted November 27, 2024; version examined: February 1, 2025.

The researchers train a teacher policy through reinforcement learning in simulation, then distill it into a policy using camera images and robot state. They deploy that policy on a Kuka arm with an Allegro hand, grasping objects with geometry, textures, and backgrounds not encountered in training. The study includes real-world lighting variation. Its simulated training creates useful physical behavior rather than merely a rendered demonstration. [Paper, sections III–V](https://arxiv.org/html/2412.01791v2).

**Engineering significance:** some skill acquisition can use parallel computational experience before deployment, reducing dependence on slow physical practice. **Boundary:** this system handles one object at a time. A surrounding state machine supplies the transport-and-deposit stages of bin packing. The authors report variable simulation-to-real transfer and remaining reliability limits; the result is a grasping capability, not a general autonomous worker. [Paper, sections IV-B and VI](https://arxiv.org/html/2412.01791v2).

### 5. AI-generated improvements already increase productive computing capacity

**AlphaEvolve, Google DeepMind.** Announced May 14, 2025; technical paper examined: June 16, 2025.

AlphaEvolve combines language models that propose code changes with automated evaluation and evolutionary selection. Its paper reports that a discovered scheduling heuristic was deployed across Google's computing fleet. Post-deployment measurements found an average recovery of **0.7% of fleet-wide compute resources** that would otherwise be stranded. Candidate heuristics were evaluated using simulation and held-out workloads before deployment. [Paper, section 3.3.1](https://arxiv.org/html/2506.13131v1).

**Engineering significance:** AI can help improve infrastructure that supplies further AI work. That is an observed feedback link between cognitive automation and productive capacity. **Boundary:** the experiment had a defined optimization problem, evaluation machinery, and an existing operational system. A useful feedback link is not proof of unrestricted recursive self-improvement or unattended industrial reproduction. [Paper, sections 2 and 3.3.1](https://arxiv.org/html/2506.13131v1).

## A technical foundation that invites construction

The following is our synthesis, not a result claimed by any one source:

1. **Specify a useful service.** Start with actual provision: moving goods, preparing components, inspecting equipment, repairing parts, or maintaining a place.
2. **Compose available capabilities.** Connect perception and planning to suitable robots, conventional controls, tools, and an environment arranged for reliable operation. A humanoid is one possible embodiment; the evidence also includes fixed arms and mobile manipulators.
3. **Learn from the work.** Measure interventions and completed service, preserve failure data, retrain or redesign, and test the resulting improvement. Skills and design knowledge can become reusable across multiple installations.
4. **Connect services into a productive network.** Automating isolated tasks becomes more consequential when their outputs reliably supply the next task. Evidence for that industrial network must include its actual missing inputs, maintenance, and human dependencies.

This is why the worlds can be presented as directions for construction. Their enabling capacities already have working components and demonstrated feedback mechanisms. A project can begin extending them without first settling the entire question of general intelligence.

“An engineering problem” has two possible meanings. If it means **a concrete program of building and testing with existing physical principles and increasingly capable methods**, the cases support it. If it means **we have established that today's available models can perform every required task and only routine integration remains**, the cases do not establish it. Engineering research can be a real route forward while still containing unresolved capability problems.

For the booklet, the stronger defensible opening is: **We already possess useful pieces of the capacity to automate provision, improve its machinery, and spread learned capability. The task is to connect and extend those pieces into systems that sustain a free and generous civilization.** Full autonomous industrial reproduction remains the project's explicit constructive hypothesis, to be tested at the network level. The social destination—secure access, freedom from compulsory wage labor, and voluntary shared undertakings—also requires institutions that turn productive power into common capability.

## Reading coverage and numerical care

Read the relevant methods, evaluation, results, and limits in the three linked technical reports; read the two Physical Intelligence primary accounts and their displayed evaluation definitions. The large publisher-hosted Gemini PDF exceeded the browsing fetch limit, so its matching arXiv HTML report was used. No benchmark is treated as a direct measurement of an entire occupation. Deployment numbers retain their original setting and reporting party. The two numerical values suitable for brief public use are the specifically reported Ultra full-shift autonomy figure and AlphaEvolve's fleet resource recovery; neither is an estimate of economy-wide automation.
