
export class APIControler {
  constructor(apiUrl = "http://localhost", port = 8000, pathname = "socios/") {
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
      console.log(content)
    } catch (error) {
      console.log(error);
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
