function bitcoinMining(goldArr) {
    const oneBitcoinPrice = 11949.16
    const oneGramGold = 67.51

    let totalMoney = 0
    let bitcoinsCount = 0
    let firstDayPuchasedBitcoin = 0
    for (let index = 0; index < goldArr.length; index++) {

        let todayGrams = goldArr[index]
        if ((index + 1) % 3 === 0) {
            todayGrams = todayGrams - ((30/100) * todayGrams)
        }

        let todayMoney = todayGrams * oneGramGold
        totalMoney += todayMoney
        
        while (totalMoney >= oneBitcoinPrice) {
            bitcoinsCount += 1

            if (!firstDayPuchasedBitcoin) {
                firstDayPuchasedBitcoin = index + 1
            }
            
            totalMoney -= oneBitcoinPrice
        }
    }

    console.log(`Bought bitcoins: ${bitcoinsCount}`)
    if (firstDayPuchasedBitcoin) {
        console.log(`Day of the first purchased bitcoin: ${firstDayPuchasedBitcoin}`)
    }
    console.log(`Left money: ${totalMoney.toFixed(2)} lv.`)
}

bitcoinMining([3124.15, 504.212, 2511.124])