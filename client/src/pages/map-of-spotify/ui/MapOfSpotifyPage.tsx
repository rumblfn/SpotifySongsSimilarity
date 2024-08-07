import {useNodesStore} from "entities/nodes";
import {Camera} from "shared/ui/camera";

export function MapOfSpotifyPage() {
  const nodes = useNodesStore(state => state.nodes)
  console.log(nodes)

  return (
    <div>
      <Camera/>
    </div>
  );
}
