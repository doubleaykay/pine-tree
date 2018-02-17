var cy = cytoscape({
  container: document.getElementById('cy'),
  elements: [
    { data: { id: 'MATH 003', class: 'MATH 003' } },
    { data: { id: 'MATH 008', class: 'MATH 008' } },
    { data: { id: 'MATH 013', class: 'MATH 013' } },
    { data: { id: 'PHYS 013', class: 'PHYS 013' } },
    { data: { id: 'PHYS 014', class: 'PHYS 014' } },
    { data: { id: 'ENGS 020', class: 'ENGS 020' } },
    { data: { id: 'ENGS 021', class: 'ENGS 021' } },
    { data: { id: 'ENGS 022', class: 'ENGS 022' } },
    { data: { id: 'ENGS 025', class: 'ENGS 025' } },
    { data: { id: 'ENGS 036', class: 'ENGS 036' } },
    { data: { id: 'CHEM 005', class: 'CHEM 005' } },
    { data: { id: 'CHEM 006', class: 'CHEM 006' } },

    { data: { id: '1', source: 'MATH 003', target: 'MATH 008' } },
    { data: { id: '2', source: 'MATH 008', target: 'MATH 013' } },
    { data: { id: '3', source: 'CHEM 005', target: 'CHEM 006' } },
    { data: { id: '4', source: 'PHYS 013', target: 'PHYS 014' } },
    {
      data: {
        id: '5',
        source: 'MATH 003',
        target: 'ENGS 021'
      }
    },
    {
      data: {
        id: '6',
        source: 'MATH 013',
        target: 'ENGS 022'
      }
    },
    {
      data: {
        id: '7',
        source: 'PHYS 014',
        target: 'ENGS 022'
      }
    },
    {
      data: {
        id: '8',
        source: 'ENGS 020',
        target: 'ENGS 022'
      }
    },
    {
      data: {
        id: '9',
        source: 'MATH 013',
        target: 'ENGS 025'
      }
    },
    {
      data: {
        id: '10',
        source: 'PHYS 014',
        target: 'ENGS 025'
      }
    },
    {
      data: {
        id: '11',
        source: 'ENGS 020',
        target: 'ENGS 025'
      }
    },
    {
      data: {
        id: '12',
        source: 'ENGS 022',
        target: 'ENGS 036'
      }
    },
    {
      data: {
        id: '13',
        source: 'ENGS 025',
        target: 'ENGS 036'
      }
    },
    {
      data: {
        id: '14',
        source: 'CHEM 005',
        target: 'ENGS 036'
      }
    },

  ],

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
