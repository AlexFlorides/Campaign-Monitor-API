/* Alexandros Florides */

function btndelete(key) {

  // unique list id
  listID = "99e10beca5f9e4eed14875b8d50d4302";
    
  url = "https://api.createsend.com/api/v3.2/subscribers/"+listID+".json?email="+key;
  // Make the HTTP Delete call using fetch api
  deleteData(url, key)
  location.reload()
}

// function that uses cors anyware api website as proxy to allow access-control and perform DELETE request to delete
// passed subscriber
function deleteData(url1, key) {

  // unique api id
  apiID = "GqtlOln5vbv3T45V80JJkVK3zAAekhhDivEP6RZjQIMnopCMaFZJ32lt0k1BL84ND2Sb31kw8gQvXLumvQtf0AeOyp04e/wbl4uBLiDHK8h1sW7xNfrAww9Pso32HVTkqdp1Q1+o6eJCGroR6LoTHA==";

  const proxyurl = "https://cors-anywhere.herokuapp.com/";  // site that doesn’t send Access-Control-*
  const url = url1; 
  fetch(proxyurl + url,{

  method:'DELETE',
  // headers for the request including basic authentication and content type
  headers: new Headers({
    'Authorization': 'Basic '+btoa(apiID+': '), 
    'Content-Type': 'application/x-www-form-urlencoded'
  })
  }
    )
    // show alert on success
  .then(alert("Subscriber: " + key + " successfuly deleted!"))
  .catch(() => console.log())
}

/* Alexandros Florides */