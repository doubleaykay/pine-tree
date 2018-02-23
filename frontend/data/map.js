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

//cy.elements().remove();
//var aaas = cy.nodes().data("id").includes("AAAS");
//var aaas = $('id').includes('AAAS');
//cy.elements().add(nodes.getElementById('MATH 013'));

var allNodes = cy.nodes();
cy.batch(function(){
  allNodes.forEach(function( n ){
    var type = n.data('NodeVisibility');
    var id = n.data("id");

    // remove the visible class from all nodes
    var makeInVisible = function(){
      n.removeClass('visible');
    };

    // make nodes visible again
    var makeVisible = function(){
      n.addClass('visible');
    };

    if ( id.includes("MATH") ){
      makeVisible();
    } else {
      makeInVisible();
    };

    if( type != 'visible' ){
      cy.elements().remove();
    };
  });
});
