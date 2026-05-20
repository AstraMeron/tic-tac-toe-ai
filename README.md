# Tic-Tac-Toe AI: Minimax with Alpha-Beta Pruning

An implementation of a turn-based, two-player, zero-sum game-playing AI for Tic-Tac-Toe. This project covers the systematic design of an adversarial agent using the Minimax algorithm and optimizes its performance through Alpha-Beta Pruning. Additionally, a comparative analysis is provided to contextualize Minimax against other advanced decision-making frameworks like Monte Carlo Tree Search (MCTS) and Markov Decision Processes (MDP).

---

## 1. Project Implementation Overview

The project was developed incrementally across four key development phases to ensure structural integrity and precise benchmarking:

* **Phase 1 (Core Board & Setup):** Built the baseline 3x3 text grid system, valid move check logic, and turn-handling routines for a standard two-player human experience.
* **Phase 2 (Standard Minimax AI):** Integrated an adversarial agent using the vanilla Minimax algorithm. The AI acts as the `Maximizer` ($O$) trying to maximize its utility score, while the human opponent acts as the `Minimizer` ($X$).
* **Phase 3 (Alpha-Beta Pruning Optimization):** Introduced alpha and beta tracking bounds to prune sub-trees that cannot influence the final optimal choice, drastically lowering the agent's computational overhead.
* **Phase 4 (Analysis & Reporting):** Collected runtime diagnostics and compiled a structural performance summary.

---

## 2. Theoretical Analysis of Tree Search Algorithms

To evaluate performance boundaries, Minimax was compared against alternative decision-making frameworks across specific structural parameters:

### A. Minimax with Alpha-Beta Pruning
* **Core Strategy:** Exhaustive, deterministic adversarial search. It builds out a full game tree under the core assumption that both players will play perfectly.
* **Alpha-Beta Efficiency:** Rather than exploring every state, it tracks two values: $\alpha$ (the minimum score the maximizing player is assured of) and $\beta$ (the maximum score the minimizing player is assured of). If a branch is found where a child node yields a worse outcome than a previously found option ($\alpha \ge \beta$), that entire branch is truncated.
* **Limitations:** It features an exponential time complexity of $O(b^d)$ (where $b$ is the branching factor and $d$ is depth). For games with large branching factors like Chess ($b \approx 35$) or Go ($b \approx 250$), searching the entire tree quickly becomes computationally intractable.

### B. Monte Carlo Tree Search (MCTS)
* **Core Strategy:** A statistical, heuristic search pattern that expands the game tree asymmetrically by prioritizing paths with higher winning potentials.
* **The Four Pillars:**
    1.  *Selection:* Traverses down the existing tree using a selection equation (like Upper Confidence Bound applied to Trees, or UCT) to maintain a balance between exploration and exploitation.
    2.  *Expansion:* Appends a new child node to the reached leaf node.
    3.  *Simulation (Rollout):* Executes a series of rapid, random moves from the expanded node until a terminal state is reached.
    4.  *Backpropagation:* Propagates the endgame result (win/loss/draw) back up to the root to adjust node statistics.
* **Key Advantage:** It is an *anytime algorithm* (can be stopped at any moment to return its best statistical guess) and requires no static state-evaluation heuristics.

### C. Markov Decision Processes (MDP)
* **Core Strategy:** A mathematical framework modeling decision-making under **probabilistic uncertainty**, defined by the tuple $(S, A, P, R, \gamma)$.
* **Key Distinctions:** Unlike Minimax, which models a conscious, adversarial opponent, an MDP models a single agent interacting with an environment where actions lead to stochastic (random or probabilistic) state transitions. It applies the *Markov Property*, meaning the next state depends solely on the current state and action, ignoring historical vectors.
* **Resolution:** Solved via Dynamic Programming (Value Iteration or Policy Iteration) to construct an optimal policy map $\pi(s)$.

---

## 3. Algorithm Comparison Matrix

| Feature | Minimax (with Alpha-Beta) | Monte Carlo Tree Search (MCTS) | Markov Decision Process (MDP) |
| :--- | :--- | :--- | :--- |
| **Environment Type** | Deterministic, Adversarial, Perfect Info | Large-Scale, Complex Game States | Stochastic, Non-Adversarial/Probabilistic |
| **Core Traversal Method**| Depth-first uniform tree traversal | Asymmetric statistical simulations (Rollouts) | Value/Policy Iteration over state matrices |
| **Evaluation Strategy** | Static terminal evaluations ($+1, -1, 0$) | Long-run win/loss statistical averages | Immediate reward signals + discounted utilities |
| **Scaling Limitations** | Impeded by massive depth or branching | Impeded by low simulation sample sizes | Impeded by memory size (State Space explosion)|
| **Suitability for Tic-Tac-Toe** | **Highly Optimal:** Instantly solves the full state space precisely. | **Overkill:** Statistical variances can cause minor sub-optimal moves. | **Overkill:** Overcomplicates a finite, non-stochastic game space. |

---

## 4. Empirical Performance & Key Metrics

Data captured from live game logs directly verifies the computational advantages of integrating Alpha-Beta bounds over standard Minimax:

* **Opening Move Computational Reduction:** During a standard Minimax run on an empty or near-empty grid, the agent evaluated up to **9,785 nodes** to select a position. Under identical constraints with Alpha-Beta Pruning enabled, the initial search space dropped significantly to **6,138 nodes**, saving nearly 37% of state traversals right at the root.
    
* **Mid-Game Pruning Acceleration:** As the game progressed and the tree depth narrowed, the alpha and beta bounds truncated dead paths aggressively. In mid-game setups, the searched node count plunged sharply:
    * Turn 3 Nodes Explored: **459**
    * Turn 5 Nodes Explored: **42**
    * Turn 7 Nodes Explored: **4** to **3**

This exponential drop shows that Alpha-Beta Pruning achieves the exact same optimal move quality as basic Minimax, while discarding redundant computations.

---

## 5. Conclusions

1.  **Optimality:** Minimax with Alpha-Beta Pruning remains the most mathematically sound approach for small, deterministic, zero-sum spaces like Tic-Tac-Toe, guaranteeing a flawless defensive profile (never losing a game if playing first or responding optimally).
2.  **Scalability Factors:** While MCTS is better suited for highly branch-dense structures (e.g., Go) and MDPs are built for environmental uncertainty (e.g., robotics or card games), Alpha-Beta Pruning effectively offsets the raw exponential costs of Minimax within narrow, perfect-information domains.