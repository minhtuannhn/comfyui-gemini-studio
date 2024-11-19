
import { app } from "/scripts/app.js";
import { $el } from "/scripts/ui.js";

/**
 * Font size of prompt fields
 */

const connectionsWidthName = "Gemini_Studio.textFields";

app.registerExtension({
  name: connectionsWidthName,
  async init(app) {
    const style = $el("style");
    document.body.append(style);
    app.ui.settings.addSetting({
      id: connectionsWidthName,
      name: "Font size for textareas",
      type: "slider",
      attrs: {
        min: 10,
        max: 24,
      },
      tooltip: "The size of the font in prompts.",
      defaultValue: 10,
      onChange(value) {
        style.innerText = `.comfy-multiline-input {font-size: ${value}px}`;
      },
    });
  },
});
