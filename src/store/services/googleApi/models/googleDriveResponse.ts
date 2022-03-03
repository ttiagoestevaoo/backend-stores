import GoogleDriveItem from "./googleDriveItem"

class GoogleDriveResponse {
    kind = ''
	incompleteSearch = false
	files: Array<GoogleDriveItem> = []
}

export default GoogleDriveResponse