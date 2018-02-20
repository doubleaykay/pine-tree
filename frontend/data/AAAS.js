var cy = cytoscape({
  container: document.getElementById('cy'),


  elements: {
    nodes: [
    { data: { id: 'AAAS 7', class: 'AAAS 7', title: 'First Year Seminar', prereqs: '', distribs: '', offered: '',}},
    { data: { id: 'AAAS 10', class: 'AAAS 10', title: 'Introduction to African-American Studies', prereqs: '', distribs: 'SOC, CI', offered: '18W, 10A'}},
    { data: { id: 'AAAS 11', class: 'AAAS 11', title: 'Introduction to African Studies', prereqs: '', distribs: 'SOC, NW', offered: '17X, 10A, 17F, 18F'}},
    { data: { id: 'AAAS 12', class: 'AAAS 12', title: 'Race and Slavery in U.S. History', prereqs: 'HIST 16', distribs: 'SOC, W', offered: '17X, 18F'}},
    ],

    edges: [
    { data: { id: '1', source: 'HIST 16', target: 'AAAS 12' } },
    { data: { id: '2', source: 'HIST 17', target: 'AAAS 13' } },
    { data: { id: '3', source: 'HIST 5.01', target: 'AAAS 14' } },
    { data: { id: '4', source: 'HIST 66', target: 'AAAS 15' } },
    { data: { id: '5', source: 'REL 14', target: 'AAAS 18' } },
    ],

  },

  style: [
    {
      selector: 'node',
      style: {
        'label': 'data(class)',
      }
    },
    {
      selector: 'edge',
      style: {
        'curve-style': 'bezier',
        'width': 4,
        'target-arrow-shape': 'triangle',
      }
    },
  ],

  layout: {
    name: 'dagre',
  },
});
