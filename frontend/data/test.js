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
    {
      data: {
        id: '1',
        source: 'MATH 003',
        target: 'MATH 008'
      }
    },
    {
      data: {
        id: '2',
        source: 'MATH 008',
        target: 'MATH 013'
      }
    },
    {
      data: {
        id: '3',
        source: 'CHEM 005',
        target: 'CHEM 006'
      }
    },
    {
      data: {
        id: '4',
        source: 'PHYS 013',
        target: 'PHYS 014'
      }
    },
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

  ],

  style: [
    {
      selector: 'node',
      style: {
        'label': 'data(class)',
      }
    }
  ],

  layout: {
    name: 'dagre',
  },
});
