// react form need to be update use dispatchEvent
// need to be paste this function to console first
const setNativeValue = (element, value) => {
  const valueSetter = Object.getOwnPropertyDescriptor(element, 'value').set;
  const prototype = Object.getPrototypeOf(element);
  const prototypeValueSetter = Object.getOwnPropertyDescriptor(prototype, 'value').set;

  if (valueSetter && valueSetter !== prototypeValueSetter) {
    prototypeValueSetter.call(element, value);
  } else {
    valueSetter.call(element, value);
  }
  element.dispatchEvent(new Event('input', { bubbles: true }));
};


// problem list : ["asd","zxc",3,4,5....]

const add = ((words) => {
  for (var i = 0; i < words.length; i++) {
    var it = document.getElementsByTagName('input')[0]
    setNativeValue(it, words[i])
    it.dispatchEvent(new Event("input", { bubbles: true }))
    var it2 = document.getElementsByTagName('input')[1]
    it2.click()
  }
})
