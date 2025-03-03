package main

// Graph представляет граф с использованием списка смежности
type Graph struct {
    vertices int
    adjList  map[int][]int
}

// NewGraph создает новый граф
func NewGraph(vertices int) *Graph {
    return &Graph{
        vertices: vertices,
        adjList:  make(map[int][]int),
    }
}

// AddEdge добавляет ребро в граф
func (g *Graph) AddEdge(v int, w int) {
    g.adjList[v] = append(g.adjList[v], w)
    g.adjList[w] = append(g.adjList[w], v) // Для неориентированного графа
}