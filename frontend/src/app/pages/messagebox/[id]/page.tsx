
interface PageProps{
    params:{id:number | string}
}
function MessageboxPage({params}:PageProps) {
    return (
       <>
       message <h1>User ID: {params.id}</h1>
       </>
    )
}

export default MessageboxPage
