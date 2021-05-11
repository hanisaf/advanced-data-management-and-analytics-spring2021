# GRAPH-TOOLS

## Presentation

You can find a link to the video presentation here:         https://youtu.be/gyOON55MvHQ

## Summary of Support Files
    
   expodemo.ipynb: the notebook referenced in the tutorial

## Guide

### What is graph-tools?

   Graph-tools is a Python module that provides tools for manipulation and statistical analysis of graphs or networks. Despite the appearance of an ordinary Python module, the algorithms at its core are actually written in C++, resulting in a much faster performance comparison. The module provides the Graph class, which supports both directed and undirected networks with multiple edges, nodes, vertex weights, and edge weights. All of its function are fully documented on the internet, and can be accessed through the help(graph_tools) function. It was originally developed for network researchers performing experiments in the field of graph theory or network science.

### Major features

   vertex operations: add, delete, degree, neighbors, random, set/get attributes
   edge operations: add, delete, random, set/get attributes
   graph operations: duplicate, adjacency matrix, diagonal matrix
   major graph operations: exploration, connectivity, maximal component, betweenness
   numerous graph generation models: random graph, Barabasi Albert
   graph import/export in GraphViz format
   
### Practical applications

   Today, networks are everywhere. Whether physical, biological, economical, or social, graph theory and network science are becoming extremely popular mathematical models for analyzing complex systems around the world. Network researchers have developed diverse techniques to address potential issues in these systems. Some examples of modern solutions may include path optimization or identifying the shortest route on a maps platform. When thinking about the recent pandemic, many people naturally apply the principles of network science when considering things like where are the biggest breakout hubs and what are the connectors between them. These are the types of questions that can efficiently be answered through network research in order to optimize these connections.
