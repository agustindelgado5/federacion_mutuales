export class Fetcher {
    constructor(
        pathname,
        url = process.env.VUE_APP_API_HOST,
        port = process.env.VUE_APP_API_PORT,
    ) {
        this.wrapperURL = new URL(url);
        this.wrapperURL.port = port;
        this.wrapperURL.pathname = pathname;
        this.accessToken = this.getJWT()
    }

    setPathname(pathname) {
        this.wrapperURL.pathname = pathname;
    }

    addParams(key, value) {
        this.wrapperURL.searchParams.append(key, value);
    }

    deleteParams(key) {
        this.wrapperURL.searchParams.delete(key)
    }

    async get() {
        try {
            let response = await fetch(this.wrapperURL, {
                method: 'GET',
                headers: { "Authorization": "Bearer " + this.accessToken, "Content-Type": "application/json", }
            });
            return response;
        } catch (error) { console.error(error); }
    }

    async post(payload) {
        try {
            let response = await fetch(this.wrapperURL, {
                method: 'POST',
                headers: { "Authorization": "Bearer " + this.accessToken, "Content-Type": "application/json", },
                body: JSON.stringify(payload)
            });
            return response;
        } catch (error) { console.error(error); }
    }

    async put(id, payload) {
        try {
            let response = await fetch(this.wrapperURL + id + "/", {
                method: 'PUT',
                headers: { "Authorization": "Bearer " + this.accessToken, "Content-Type": "application/json", },
                body: JSON.stringify(payload)
            });
            return response;
        } catch (error) { console.error(error); }
    }

    async delete(id) {
        try {
            let response = await fetch(this.wrapperURL + id + "/", {
                method: 'DELETE',
                headers: { "Authorization": "Bearer " + this.accessToken, "Content-Type": "application/json", },
            });
            return response;
        } catch (error) { console.error(error); }
    }

    async getList() {
        try {
            let response = await this.get()
            let json = await response.json();
            return json.results;

        } catch (error) { console.error(error); }
    }

    async createJWT(payload) {
        try {
            this.setPathname("auth/jwt/create")
            let response = await this.post(payload)
            let json = await response.json();

            this.accessToken = json.access
            sessionStorage.setItem('accessToken', this.accessToken)

            return json.access;
        } catch (error) { console.error(error); }
    }

    deleteJWT() {
        sessionStorage.removeItem('accessToken')
    }

    getJWT() {
        return sessionStorage.getItem('accessToken')
    }

    async login(payload) {
        return await this.createJWT(payload)
    }
    logout() {
        this.deleteJWT()
    }
    isLogged() {
        let token = this.getJWT()
        return (!token || token == {} || token == [] || token === 'undefined' || token === null) ? false : true
    }
}