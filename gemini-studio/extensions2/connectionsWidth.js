 
import { app } from "/scripts/app.js";

/**
 * Connections Width
 */

const connectionsWidthName = "Gemini_Studio.ConnectionsWidth";

app.registerExtension({
  name: connectionsWidthName,
  async init(app) {
    app.ui.settings.addSetting({
      id: connectionsWidthName,
      name: "Connectors Width",
      type: "slider",
      attrs: {
        min: 2,
        max: 12,
      },
      tooltip: "The width of connector lines.",
      defaultValue: 3,
      onChange(value) {
        app.canvas.connections_width = +value;
        app.graph.setDirtyCanvas(true, true);
      },
    });
  },
});
