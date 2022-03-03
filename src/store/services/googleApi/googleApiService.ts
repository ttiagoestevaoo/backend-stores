import Service from "../service"
import GoogleDriveResponse from "./models/googleDriveResponse"

/* eslint-disable @typescript-eslint/no-explicit-any */
class GoogleApiService extends Service {
    key = "AIzaSyAr-u6hVWrKlBJML48H1lVYhmTvqQUHvMo"
    constructor() {
        super("https://www.googleapis.com")
    }

    async getAlbumFiles(id: string) : Promise<GoogleDriveResponse>{
        const response: any= ( await this.http.get(`drive/v3/files/?key=${this.key}&includeItemsFromAllDrives=true&supportsAllDrives=true&q="${id}" in parents and mimeType="image/jpeg"`)).data
        return response
    }
        
}

export default GoogleApiService