import React, {useEffect} from 'react'
import {clickButtonNode, getNodeList} from "../redux/node-reducer";
import {compose} from "redux";
import {connect} from "react-redux";

const NodeList = ({nodes, getNodeList, clickButtonNode, ...props}) => {
    useEffect( () => getNodeList(), [getNodeList])
    return (
        <div className="row m-2">
            {nodes.map((node) =>
                <div className="col-md-4" key={node.id}>
                    <button className="btn btn-info btn_home"
                       onClick={() => clickButtonNode(node.id)}>
                        {node.title}
                    </button>
                </div>
            )}
        </div>
    )
}


let mapStateToProps = (state) => {
    return {
        nodes: state.node.nodes,
    }
}

export default compose(connect(mapStateToProps,
    { getNodeList, clickButtonNode }))(NodeList);
