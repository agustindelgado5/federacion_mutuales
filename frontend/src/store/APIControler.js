import swal from "sweetalert";
export class APIControler {
  constructor(apiUrl = "http://localhost", port = 8081, pathname = "socios/") {
    this.apiUrl = new URL(apiUrl);
    this.apiUrl.port = port;
    this.apiUrl.pathname = pathname;
  }

  addSearchParams(key, value) {
    this.apiUrl.searchParams.append(key, value);
  }

  deleteSearchParams(key) {
    this.apiUrl.searchParams.delete(key);
  }

  async getData() {
    try {
      let response = await fetch(this.apiUrl);
      let data = await response.json();

      return data.results;
    } catch (error) {
      console.log(error);
    }
  }

  async postData(payload) {
    try {
        console.log(JSON.stringify(payload))
      let response = await fetch(this.apiUrl, {
        method: "POST",
        headers: {
          "Accept": "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload)
      });
      const content = await response.json();
      if(response.ok)
      {
        swal("Carga Exitosa", " ", "success")
        console.log(content)
      }
      else{
        console.log(content);
        swal("¡ERROR!", "Los datos no son válidos" , "error")
        return content;
      }
      //location.href = '/socios'
      
      
    } catch (error) {
      swal("¡ERROR!", "Se ha detectado un problema ", "error")
      console.log(error);
      //swal("¡ERROR!", "{error}", "error")
    }
    
  }

  async putData(payload) {
    try{
      let response = await fetch(this.apiUrl + payload.id, {
        method: "PUT",
        body: JSON.stringify(payload),
        headers: {
          "Accept": "application/json",
          "Content-Type": "application/json",
        },
      })
    }catch (error) {

    }
  }

}
