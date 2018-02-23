var GraphStyle = [
  {
    selector: 'node',
    style: {
      'label': 'data(class)',
      'background-color': function( e ){
        return e.data("id").includes("AAAS")?"red":
        e.data("id").includes("ANTH")?"red":
        e.data("id").includes("ARTH")?"red":
        e.data("id").includes("AMEL")?"red":
        e.data("id").includes("ARAB")?"red":
        e.data("id").includes("CHIN")?"red":
        e.data("id").includes("HEBR")?"red":
        e.data("id").includes("JAPN")?"red":
        e.data("id").includes("AMES")?"red":
        e.data("id").includes("BIOL")?"green":
        e.data("id").includes("CHEM")?"blue":
        e.data("id").includes("CLST")?"red":
        e.data("id").includes("GRK")?"red":
        e.data("id").includes("LAT")?"red":
        e.data("id").includes("COGS")?"red":
        e.data("id").includes("COCO")?"red":
        e.data("id").includes("COLT")?"red":
        e.data("id").includes("COSC")?"purple":
        e.data("id").includes("INTS")?"red":
        e.data("id").includes("EARS")?"red":
        e.data("id").includes("ECON")?"red":
        e.data("id").includes("EDUC")?"red":
        e.data("id").includes("ENGS")?"orange":
        e.data("id").includes("ENGL")?"red":
        e.data("id").includes("ENVS")?"red":
        e.data("id").includes("FILM")?"red":
        e.data("id").includes("FREN")?"red":
        e.data("id").includes("FRIT")?"red":
        e.data("id").includes("ITAL")?"red":
        e.data("id").includes("GEOG")?"red":
        e.data("id").includes("GERM")?"red":
        e.data("id").includes("GOVT")?"red":
        e.data("id").includes("HIST")?"red":
        e.data("id").includes("HUM")?"red":
        e.data("id").includes("JWST")?"red":
        e.data("id").includes("LACS")?"red":
        e.data("id").includes("LATS")?"red":
        e.data("id").includes("LING")?"red":
        e.data("id").includes("MATH")?"pink":
        e.data("id").includes("MUS")?"red":
        e.data("id").includes("NAS")?"red":
        e.data("id").includes("PHIL")?"red":
        e.data("id").includes("ASTR")?"red":
        e.data("id").includes("PHYS")?"yellow":
        e.data("id").includes("PSYC")?"red":
        e.data("id").includes("QSS")?"red":
        e.data("id").includes("PBPL")?"red":
        e.data("id").includes("REL")?"red":
        e.data("id").includes("RUSS")?"red":
        e.data("id").includes("SSOC")?"red":
        e.data("id").includes("SOCY")?"red":
        e.data("id").includes("SPAN")?"red":
        e.data("id").includes("PORT")?"red":
        e.data("id").includes("SART")?"red":
        e.data("id").includes("THEA")?"red":
        e.data("id").includes("TUCK")?"red":
        e.data("id").includes("WGSS")?"red":
        e.data("id").includes("SPEE")?"red":
        e.data("id").includes("WRIT")?"red":"red";
      },
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
]
