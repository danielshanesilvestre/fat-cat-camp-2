import {useEffect, useState} from "react";



function OwnersIndex() {

  useEffect(() => {
    fetch("/api/owners")
      .then(response => response.json())
      .then(data => {
        console.log(data);
      })

  }, [])

  return <>

  </>
}

export default OwnersIndex;