import {useNodesStore} from "entities/nodes";

export function MapOfSpotifyPage() {
  const nodes = useNodesStore(state => state.nodes)
  console.log(nodes)

  return (
    <div className="page">

    </div>
  );
}
