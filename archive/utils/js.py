set_webdriver_js_script = """Object.defineProperty(navigator, "webdriver", {
  get: () => false,
})"""

scroll_to_end_js_script = """
async () => {
  await new Promise(resolve => {
    let totalHeight = 0;
    const distance = 500;
    const timer = setInterval(() => {
      const scrollHeight = document.body.scrollHeight;
      window.scrollBy(0, distance);
      totalHeight += distance;

      if (totalHeight >= scrollHeight) {
        clearInterval(timer);
        resolve();
      }
    }, 100);
  });
}"""
get_page_scrollHeight = "() => document.documentElement.scrollHeight"
get_page_scrollWidth = "() => document.documentElement.scrollWidth"
