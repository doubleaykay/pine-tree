var cy = cytoscape({
  container: document.getElementById('cy'),

  //layout: {
    //name: 'klay',
  //},

  style: GraphStyle,

  elements: {
    nodes: nodes,
    edges: edges,
  },
});

var layout = cy.layout({
  name: 'klay'
});
layout.run();

function filterMath() {
  var checkBox = document.getElementById("checkMath");
  var math = cy.filter(function( n ){
    if(n.data("target")){
      return n.data("target").includes("MATH")||n.data("source").includes("MATH");
    } else {
      return n.data("id").includes("MATH");
    }
  });
  if (checkBox.checked){
    math.restore();
    //layout.run();
  } else {
    math.remove();
    //layout.run();
  }
}
