
import { app } from "/scripts/app.js";

const renderShadowsName2 = "Gemini_Studio.RenderShadows";

app.registerExtension({
  name: renderShadowsName2,
  async init(app) {
    app.ui.settings.addSetting({
      id: renderShadowsName2,
      name: "Tạo Bóng Đổ cho Node",
      type: "boolean",
      tooltip: "Hiện / Ẩn bóng đổ cho Node",
      defaultValue: true,
      onChange(value) {
        app.canvas.render_shadows = value;
        app.graph.setDirtyCanvas(true, true);
      },
    });
 
  },
});
