"use strict";

const HOST = "http://localhost:5000";

const tweet = (text) => {
	const url = `${HOST}/post`;
	fetch(url, {
		method: "POST",
		body: text,
		credentials: "include"
	}).then(response => {
		return response.json();
	}).then(json => {
		console.log(json);
	});
};


const delete_msg = (kind) => {
	const msg = document.getElementById(kind);
	msg.parentNode.removeChild(msg);
};

const put_senryus = (senryus) => {
	const table = document.querySelector("table");
	const append_senryu = (senryu, n) => {
		const row = document.createElement("tr");
		const text = document.createElement("td");
		text.innerText = senryu;
		text.setAttribute("id", `sen${n}`);

		const post = document.createElement("td");
		const button = document.createElement("button");
		button.innerText = "tweet";
		button.setAttribute("class", "btn-post");
		
		post.appendChild(button);
		row.appendChild(text);
		row.appendChild(post);
		table.appendChild(row);
	};

	let i = 0;
	for (const senryu of senryus) {
		append_senryu(senryu, i++);
	}
};

const enable_post_button = () => {
	// for tweet button
	const btns = document.getElementsByClassName("btn-post");
	const fn_btn = (e) => {
		// td->button
		const tag = e.currentTarget;
		// td(tweet content)
		const text = tag.parentElement.previousElementSibling.innerText;

		if (confirm(`「${text}」をツイートしますか?`)) {
			tweet(text);
		}
	};
	for (const btn of btns) {
		btn.addEventListener("click", fn_btn, false);
	}
};

//TODO: ログイン前はリクエストを飛ばさない
const get_senryu = () => {
	const url = `${HOST}/senryu`;
	fetch(url, {
		credentials: "include"
	})
	.then(response => response.json())
	.then(senryus => {
		if (senryus) {
			put_senryus(senryus);
			enable_post_button();
			delete_msg("msg-pending");
		}
	});
};

document.addEventListener("DOMContentLoaded", function() {
	get_senryu();
});
