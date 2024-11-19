
import { app } from "/scripts/app.js";

/**
 * Pin/Unpin all nodes on canvas
 */

const pinNodesName = "Gemini_Studio.pinNodes";

app.registerExtension({
  name: pinNodesName,
  async setup(app) {
    const getCanvasMenuOptions = LGraphCanvas.prototype.getCanvasMenuOptions;
    LGraphCanvas.prototype.getCanvasMenuOptions = function () {
      const menuOptions = getCanvasMenuOptions.apply(this, arguments);
      menuOptions.push(
        null,
        {
          content: "Pin all Nodes",
          callback: () => {
            app.graph._nodes.forEach((node) => {
              node.flags.pinned = true;
            });
          },
        },
        {
          content: "Unpin all Nodes",
          callback: () => {
            app.graph._nodes.forEach((node) => {
              node.flags.pinned = false;
            });
          },
        }
      );

      return menuOptions;
    };
  },
});
