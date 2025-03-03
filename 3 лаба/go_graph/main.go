package main

import "fmt"

func main() {
    // Создаем граф
    g := NewGraph(6)
    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(3, 4)

    // Находим компоненты связности
    fmt.Println("Компоненты связности в графе:")
    g.FindConnectedComponents()
}