# Network-Simulation-Analysis
This project explores the implementation and further study of networks based on a current university module using networkx and osmnx


## Basic Microscopic Structural Characteristics 

### Node Degrees & Neighbourhoods
* **Directed Graphs:**
  * **In-degree:** $k_i^{\text{in}}(A) = \sum_{j=1}^N A_{ij}$ (arrows entering $i$).
  * **Out-degree:** $k_i^{\text{out}}(A) = \sum_{j=1}^N A_{ji}$ (arrows leaving $i$).
  * **In-/Out-neighbourhoods:** $\partial_i^{\text{in}}(A) = \{j \in V : A_{ij} = 1\}$ and $\partial_i^{\text{out}}(A) = \{j \in V : A_{ji} = 1\}$.
* **Nondirected Graphs:** $k_i^{\text{in}}(A) = k_i^{\text{out}}(A) = k_i(A) = \sum_{j=1}^N A_{ij}$.
  * For simple nondirected graphs, $k_i(A) = (A^2)_{ii}$.

### Local Clustering Coefficient & Triangles
* **Number of Triangles ($T_i$):** For a simple nondirected graph:
  $$T_i(A) = \frac{1}{2} \sum_{j,k \neq i} (1 - \delta_{j,k}) A_{ij} A_{jk} A_{ki} = \frac{1}{2}(A^3)_{ii}$$
* **Local Clustering Coefficient ($C_i$):** The fraction of distinct neighbour pairs of node $i$ that are themselves connected ($C_i \in [0,1]$):
  $$C_i(A) = \begin{cases} \dfrac{2 T_i(A)}{k_i(A)[k_i(A) - 1]} & \text{if } k_i(A) > 1, \\ 0 & \text{if } k_i(A) \in \{0, 1\}. \end{cases}$$

### Graph Distance & Path-Based Centralities
* **Geodesic Distance ($d_{ij}$):** The length of the shortest path between nodes $i$ and $j$ (smallest integer $l \ge 0$ such that $(A^l)_{ij} > 0$, or $\infty$ if disconnected).
* **Closeness Centrality ($x_i$):** Inverse of the average shortest path distance from node $i$ to all other nodes (defined on connected graphs):
  $$x_i(A) = \frac{1}{d_i(A)}, \qquad d_i(A) = \frac{1}{N} \sum_{j=1}^N d_{ij}(A)$$
* **Betweenness Centrality ($y_i$):** Measures how frequently node $i$ acts as a bridge along shortest paths between all node pairs $(j,l)$:
  $$y_i(A) = \sum_{j=1}^N \sum_{l=1}^N \frac{n_i(j,l; A)}{g(j,l; A)}$$
  where $g(j,l; A)$ is the total number of geodesics from $l$ to $j$, and $n_i(j,l; A)$ is the number passing through $i$.


---
