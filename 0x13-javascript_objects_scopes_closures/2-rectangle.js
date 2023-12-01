#!/usr/bin.node
/* A class Rectangle that defines a rectangle
 */

class Rectangle {
	constructor (w, h) {
		if (h > 0 && w > 0) {
			this.height = h;
			this.width = w;
		}
	}
}

module.exports = Rectangle;
