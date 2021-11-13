export class Fetcher {
    constructor(
        url = process.env.VUE_APP_API_URL,
        port = process.env.VUE_APP_API_PORT,
    ) {
        this.wrapperURL = new URL(url);
        this.wrapperURL.port = port;
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

    async fetch() {
        try {
            let response = await fetch(this.wrapperURL, {
                method: 'GET',
                // headers: { "Authorization": "Bearer " + this.accessToken }
            });

            return response;
        } catch (error) {
            console.error(error);
        }
    }
}