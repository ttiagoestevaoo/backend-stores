import axios, { AxiosInstance } from 'axios'

abstract class Service {
    protected http: AxiosInstance
    protected url: string

    constructor(url: string) {
        this.url = url
        this.http = axios.create({
            baseURL: this.url,
        });
    }

}

export default Service
