/**
 * Function to post the selected file back to TinyMCE
 */
    var FileBrowserDialogue = {
        fileSubmit : function (FileURL) {
            window.parent.postMessage({
                mceAction: 'FileSelected',
                content: FileURL
                }, window);/*<- the star is a security issue, MUST send some valid origin to prevent message injection*/
        }
    }
