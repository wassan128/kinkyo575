"use strict";

//const HOST = "http://localhost:5000";
const HOST = "https://kinkyo575.herokuapp.com";
const OPEN = 1;
const CLOSE = 0;

const sleep = (msec) => {
	return new Promise((resolve, reject) => {
		setTimeout(resolve, msec);
	});
};

const delete_msg = (kind) => {
	const msg = document.getElementById(kind);
	msg.parentNode.removeChild(msg);
};

const append_msg = (kind, txt) => {
	const msg = document.getElementById(kind);
	msg.innerText = txt;
	msg.style.display = "block";

	sleep(3000).then(() => {
		msg.style.display = "none";
	});
}

const put_senryus = (senryus) => {
	const wrap = document.querySelector(".wrapper");
	const append_senryu = (senryu, n) => {
		const text = document.createElement("p");
		text.innerText = senryu;
		text.setAttribute("id", `sen${n}`);
		text.setAttribute("class", "cards btn-post");

		wrap.appendChild(text);
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
		const text = e.currentTarget.innerText;
		const h3 = document.getElementById("conf-txt");
		h3.innerText = text;

		set_modal(OPEN);
	};
	for (const btn of btns) {
		btn.addEventListener("click", fn_btn, false);
	}
};

const set_modal = (op) => {
	const wnd = document.getElementById("modal-wrap");
	if (op == CLOSE) {
		wnd.style.display = "none";
	} else {
		wnd.style.display = "block";
	}
};

const tweet = (text) => {
	const url = `${HOST}/post`;
	fetch(url, {
		method: "POST",
		body: text,
		credentials: "include"
	}).then(response => {
		return response.json();
	}).then(json => {
		if (json["res"] == "ok") {
			append_msg("msg-status", "ツイートしました。");
		} else {
			append_msg("msg-status", "ツイートに失敗しました。")
		}
	});
};

const en_cont = () => {
	const b_yes = document.getElementById("confirm-ok");
	b_yes.addEventListener("click", () => {
		const text = document.getElementById("conf-txt").innerText;
		tweet(text);
		set_modal(CLOSE);
	});
	const b_no = document.getElementById("confirm-ng");
	b_no.addEventListener("click", () => {
		set_modal(CLOSE);
	});
};

const get_senryu = () => {
	const url = `${HOST}/senryu`;
	fetch(url, {
		credentials: "include"
	})
	.then(response => response.json())
	.then(senryus => {
		if (senryus) {
			delete_msg("msg-pending");
			if (senryus.length !== 0) {
				put_senryus(senryus);
				enable_post_button();
			} else {
				document.querySelector(".no-senryu").style.display = "block";
			}
		} else {
			document.querySelector(".no-senryu").style.display = "block";
		}
	});
};

document.addEventListener("DOMContentLoaded", () => {
	en_cont();
	get_senryu();
});