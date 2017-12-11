"use strict";

const HOST = "http://localhost:5000";

document.addEventListener("DOMContentLoaded", function() {
	const get_senryu = () => {
		const url = `${HOST}/hoge`;
		fetch(url, {
			credentials: "include"
		}).then(response => {
			return response.json();
		}).then(json => {
			console.log(json);
		});
	};
	get_senryu();

	// tweet
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
	Array.from(btns).forEach((btn) => {
		btn.addEventListener("click", fn_btn, false);
	});

});
