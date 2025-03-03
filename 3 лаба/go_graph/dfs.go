package main

import "fmt"

// DFS выполняет обход графа в глубину
func (g *Graph) DFS(v int, visited map[int]bool) {
    visited[v] = true
    fmt.Printf("%d ", v)

    for _, neighbor := range g.adjList[v] {
        if !visited[neighbor] {
            g.DFS(neighbor, visited)
        }
    }
}

// FindConnectedComponents находит все компоненты связности в графе
func (g *Graph) FindConnectedComponents() {
    visited := make(map[int]bool)
    componentID := 0

    for v := 0; v < g.vertices; v++ {
        if !visited[v] {
            fmt.Printf("Компонента связности %d: ", componentID)
            g.DFS(v, visited)
            fmt.Println()
            componentID++
        }
    }
}