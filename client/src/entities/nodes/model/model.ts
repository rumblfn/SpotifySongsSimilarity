import { create } from 'zustand'
import { Node } from "shared/types/node.ts";
import nodes from 'shared/assets/json/nodes.json'

type Store = {
  nodes: Node[],
}

export const useNodesStore = create<Store>()((
  // set
) => ({
  nodes: nodes,
}))