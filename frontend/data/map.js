var cy = cytoscape({
  container: document.getElementById('cy'),

  layout: {
    name: 'klay',
  },

  style: GraphStyle,

  elements: {
    nodes: nodes,
    edges: edges,
  },
});
