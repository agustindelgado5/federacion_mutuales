export class Fetcher {
    constructor(
        pathname,
        url = process.env.VUE_APP_API_HOST,
        port = process.env.VUE_APP_API_PORT,
    ) {
        this.wrapperURL = new URL(url);
        this.wrapperURL.port = port;
        this.wrapperURL.pathname = pathname;
        // this.accessToken = loadSessionStorage().access
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
                // headers: { "Authorization": "Bearer " + this.accessToken }
            });
            return response;
        } catch (error) { console.error(error); }
    }

    async post(payload) {
        try {
            let response = await fetch(this.wrapperURL, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(payload)
            });
            return response;
        } catch (error) { console.error(error); }
    }

    async put(id, payload) {
        try {
            let response = await fetch(this.wrapperURL + id + "/", {
                method: 'PUT',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(payload)
            });
            return response;
        } catch (error) { console.error(error); }
    }

    async delete(id) {
        try {
            let response = await fetch(this.wrapperURL + id + "/", {
                method: 'DELETE',
            });
            return response;
        } catch (error) { console.error(error); }
    }

    async getList() {
        let response = await this.get()
        let json = await response.json();
        return json.results;
    }
}