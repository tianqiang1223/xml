import xml.dom.minidom as xmldom
import os

# 读取
def read(Anns=None):
	for Ann in Anns:
		dom_Tree = xmldom.parse('xml' + '/' + Ann)
		root = dom_Tree.documentElement
		objs = root.getElementsByTagName("bndbox")
		for obj in objs:
			name = obj.getElementsByTagName("xmin")[0].childNodes[0].data
			print(name)

# 更新
def update(Anns=None):
	if not os.path.exists("update"):
		os.mkdir("update")
	for Ann in Anns:
		dom_Tree = xmldom.parse('xml' + '/' + Ann)
		root = dom_Tree.documentElement

		objs = root.getElementsByTagName("object")
		for obj in objs:
			name = obj.getElementsByTagName("name")[0].childNodes[0].data
			if name == "rough_scratches":
				obj.getElementsByTagName("name")[0].childNodes[0].data = "scratches"
			elif name == "fine_scratches":
				obj.getElementsByTagName("name")[0].childNodes[0].data = "scratches"

			elif name == "big_stain":
				obj.getElementsByTagName("name")[0].childNodes[0].data = "stain"
			elif name == "small_stain":
				obj.getElementsByTagName("name")[0].childNodes[0].data = "stain"

			elif name == "rough_ripples":
				obj.getElementsByTagName("name")[0].childNodes[0].data = "ripples"
			elif name == "fine_ripples":
				obj.getElementsByTagName("name")[0].childNodes[0].data = "ripples"

# 写入 write
			with open("update" + '/' + Ann, 'w') as f:
				dom_Tree.writexml(f, addindent="  ", encoding='UTF8')

# 插入  Insert
def insert(Anns=None):
	if not os.path.exists("insert"):
		os.mkdir("insert")
	for Ann in Anns:
		dom_Tree = xmldom.parse('xml' + '/' + Ann)
		root = dom_Tree.documentElement

		new_watermark_node = dom_Tree.createElement("object")

		new_name = dom_Tree.createElement("name")
		new_name_text = dom_Tree.createTextNode("watermark")
		new_name.appendChild(new_name_text)
		new_watermark_node.appendChild(new_name)

		new_pose = dom_Tree.createElement("pose")
		new_pose_text = dom_Tree.createTextNode("Unspecified")
		new_pose.appendChild(new_pose_text)
		new_watermark_node.appendChild(new_pose)

		new_truncated = dom_Tree.createElement("truncated")
		new_truncated_text = dom_Tree.createTextNode('0')
		new_truncated.appendChild(new_truncated_text)
		new_watermark_node.appendChild(new_truncated)

		new_difficult = dom_Tree.createElement("difficult")
		new_difficult_text = dom_Tree.createTextNode('0')
		new_difficult.appendChild(new_difficult_text)
		new_watermark_node.appendChild(new_difficult)

		new_bndbox = dom_Tree.createElement("bndbox")

		new_xmin = dom_Tree.createElement("xmin")
		new_xmin_text = dom_Tree.createTextNode("1")
		new_xmin.appendChild(new_xmin_text)
		new_bndbox.appendChild(new_xmin)

		new_ymin = dom_Tree.createElement("ymin")
		new_ymin_text = dom_Tree.createTextNode("1")
		new_ymin.appendChild(new_ymin_text)
		new_bndbox.appendChild(new_ymin)

		new_xmax = dom_Tree.createElement("xmax")
		new_xmax_text = dom_Tree.createTextNode("100")
		new_xmax.appendChild(new_xmax_text)
		new_bndbox.appendChild(new_xmax)

		new_ymax = dom_Tree.createElement("ymax")
		new_ymax_text = dom_Tree.createElement("100")
		new_ymax.appendChild(new_ymax_text)
		new_bndbox.appendChild(new_ymax)

		new_watermark_node.appendChild(new_bndbox)

		root.appendChild(new_watermark_node)

# 写入 write
		with open("insert" + '/' + Ann, 'w') as f:
			dom_Tree.writexml(f, addindent="  ", encoding='UTF8')


if __name__ == "__main__":
	path = 'xml'
	Anns = os.listdir(path)
	read(Anns)
	update(Anns)
	insert(Anns)
