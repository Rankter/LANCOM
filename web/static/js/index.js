/*
* WebChat
* */
// 创建一个WebSocket对象，连接到服务器
const hostname = window.location.hostname
var ws = new WebSocket("ws://"+hostname+":8305", );
// 当WebSocket连接建立时，显示连接成功的消息
ws.onopen = function() {
	console.log("连接成功")
	$('#link_status').addClass('on')
};
// 当WebSocket连接关闭时，显示连接断开的消息
ws.onclose = function() {
	console.log("断开链接")
	$('#link_status').removeClass('on')
};

function show_msg_docum_func(avatar, avatar_img, send_data){
	let show_msg_docm = null
	show_msg_docm = send_data + '<img class="avatar" src="'+avatar_img+'" alt="我">'
	if (avatar === 'me') {
			show_msg_docm = send_data + '<img class="avatar" src="'+avatar_img+'" alt="我">'
	}else if(avatar === 'she'){
			show_msg_docm = '<img class="avatar" src="'+avatar_img+'" alt="她">\n' + send_data
	}
	return show_msg_docm
}
// 当WebSocket接收到服务器发送的消息时，显示消息内容
ws.onmessage = function(event) {
	let msg = event.data
	console.log(msg)
	let json_msg = JSON.parse(msg)
	$main_ul = $('#show_chat_model .main_UL')
	let send_data = ''
	if(json_msg["type"] === 'image'){
		let img_src = json_msg['img_src']
		send_data = '<img src="'+img_src+'" style="max-width: 300px;" alt="">'
	}else if(json_msg["type"] === 'file'){
		let file_path = json_msg['file_path']
		let file_name = json_msg['file_name']
		let file_type = json_msg['file_type']
		send_data = '<div class="message">\n' +
            '<a href="'+file_path+'" class="flex_center" target="_blank">\n' +
            '   <img class="file" src="static/images/file/'+file_type+'" alt="">\n' +
            '</a>\n' +
            '<span class="text">'+file_name+'</span>\n' +
            '</div>'
	}else{
		let msg_text = json_msg["text"].replace(/\n/g,"<br/>")
		send_data = '<div class="message">'+msg_text+'</div>\n'
	}
	let avatar = json_msg["avatar"]
	let avatar_img = json_msg["avatar_img"]
	let show_msg_docm = show_msg_docum_func(avatar, avatar_img, send_data)
	$main_ul.append('<li class="my_clear">\n' +
		'            <div class="'+json_msg["avatar"]+'">\n' +
		'                <p class="c_time">'+json_msg["c_time"]+'</p>\n' +
		'                <div class="msg_title">\n' + show_msg_docm +
		'                </div>\n' +
		'            </div>\n' +
		'        </li>')
	$('textarea[name="msg_text"]').val('')
};
// 获取按钮对象
$fasong_btn = $('#send_msg_model .sct .icon-fasong')
$sucai_btn = $('#send_msg_model .sct .icon-sucai')
$fasong_btn.click(function () {
    console.log('发送信息')
    let msg_text = $('textarea[name="msg_text"]').val().trim()
    if (msg_text !== ''){
        let message = JSON.stringify({"type":"text", "content": msg_text})
        ws.send(message);
    }else{
        alert('The content sent cannot be empty')
    }
})
// 上传文件
$sucai_btn.click(function () {
    console.log('选择发送文件')
    $file_up = $('#file-upload')
    $file_up.click();
    $file_up.change(function () {
        // $('#progress_screen').removeClass('on')
        //获取所有文件
        let fileList = document.getElementById("file-upload").files;
        //循环发送
        let total = fileList.length
        if (fileList) {
            for (let i = 0; i < total; i++) {
                readFile(fileList[i]);
            }
        }
        $('#file-upload').val('')
    });
})

function readFile(file) {
    var reader = new FileReader();
    reader.readAsArrayBuffer(file);
    reader.onload = function (e) {
        ws.send(JSON.stringify({"type":"file_name", "content": file.name}));//send()方法发送文件名给服务器
        let fileData = reader.result;
        // ws.send(fileData)
		var date = [];
		var n = 1000;
		//将获取的二进制按1000等分，合并成数组
		//因为字节太长，后台接收不到
		for (var i = 0, l = fileData.byteLength; i < l / n; i++) {
		   var a = fileData.slice(n * i, n * (i + 1));
			  date.push(a);
		}
		//将等分好的数组，循环发送给服务器
		for (i = 0; i < date.length; i++) {
			 ws.send(date[i])
		}
        // console.log('发送' + file.name + '成功!');
		let ext = file.name.substr(file.name.lastIndexOf('.')+1)
		if (isAssetTypeAnImage(ext)){
        	ws.send(JSON.stringify({"type":"image"}))
		}else {
			ws.send(JSON.stringify({"type":"file"}))
		}
	}
 }
function isAssetTypeAnImage(ext){
	return [
		'WEBP','BMP','PCX','TIF', 'GIF','JPG','JPGE', 'JPEG', 'TGA','EXIF','FPX','SVG','PSD',
		'CDR','PCD','DXF', 'UFO', 'EPS', 'AI', 'PNG', 'HDRI', 'RAW', 'WMF',
		'FLIC','EMF', 'ICO'
	].indexOf(ext.toUpperCase()) !== -1
}
// 关闭进度条展示
$('#close_progress_bar').click(function () {
	$('#progress_screen').addClass('on')
})


// 滚动条事件
$(window).scroll(function() {
	// 获取 document 的高度
	let docHeight = $(document).height();
	// 获取 window 的高度
	let winHeight = $(window).height();
	// 获取滚动条的位置, 距离顶部的距离
	let scrollTop = $(window).scrollTop();
	// 判断滚动条是否接近底部
    // console.log('docHeight', docHeight)
    // console.log('winHeight', winHeight)
    // console.log('scrollTop', scrollTop)
	if (docHeight - (winHeight + scrollTop) <= 5) {
        var msg_text = document.getElementById('msg_text');
        if (msg_text !== document.activeElement) {
        	if(docHeight > winHeight){
            	$('#send_msg_model .shell').addClass('on')
        	}
        }
	}else if(scrollTop === 0){
        $('#send_msg_model .shell').removeClass('on')
    }else{
		$('#send_msg_model .shell').removeClass('on')
	}
});

// 格式化换行显示
$('.message.text').each(function (index,element) {
	let msg_text = $(this).html().trim()
	// console.log(msg_text.replace(/\n/g, '<br/>'))
	$(this).html(msg_text.replace(/\n/g, '<br/>'))
})