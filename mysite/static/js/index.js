let date = new Date();

const renderCalender = () => {
    const viewYear = date.getFullYear();
    const viewMonth = date.getMonth();
    const viewDay = date.getDay();

    document.querySelector(".year-month").textContent = `${viewYear}년 ${
    viewMonth + 1
  }월`;

    const prevLast = new Date(viewYear, viewMonth, 0);
    const thisLast = new Date(viewYear, viewMonth + 1, 0);

    const PLDate = prevLast.getDate();
    const PLDay = prevLast.getDay();

    const TLDate = thisLast.getDate();
    const TLDay = thisLast.getDay();

    const prevDates = [];
    const thisDates = [...Array(TLDate + 1).keys()].slice(1);
    const nextDates = [];

    if (PLDay !== 6) {
        for (let i = 0; i < PLDay + 1; i++) {
            prevDates.unshift(PLDate - i);
        }
    }

    for (let i = 1; i < 7 - TLDay; i++) {
        nextDates.push(i);
    }

    const dates = prevDates.concat(thisDates, nextDates);
    const firstDateIndex = dates.indexOf(1);
    const lastDateIndex = dates.lastIndexOf(TLDate);

    dates.forEach((date, i) => {
        const condition =
            i >= firstDateIndex && i < lastDateIndex + 1 ? "this" : "other";
        dates[
            i
        ] = `<form name="search-form" id="${date}" method="POST" class="date">
                <input type="hidden" name="year" value=${viewYear}>
                <input type="hidden" name="month" value=${viewMonth+1}>
                <input type="hidden" name="date" value=${date}>
                <div class=${condition} id="thisdate" onClick="document.forms[${date}].submit();">
                    ${date}
                </div>
    </form>`;
        // ] = `<form class="date"><span class=${condition} id="thisdate" onclick="alert('you clicked inside the header');">${date} </span></form>`;
    });

    document.querySelector(".dates").innerHTML = dates.join("");

    const today = new Date();
    if (viewMonth === today.getMonth() && viewYear === today.getFullYear()) {
        for (let date of document.querySelectorAll(".this")) {
            if (+date.innerText === today.getDate()) {
                date.classList.add("today");
                break;
            }
        }
    }
};

renderCalender();

const prevMonth = () => {
    date.setDate(1);
    date.setMonth(date.getMonth() - 1);
    renderCalender();
};

const nextMonth = () => {
    date.setDate(1);
    date.setMonth(date.getMonth() + 1);
    renderCalender();
};

const goToday = () => {
    date = new Date();
    renderCalender();
};