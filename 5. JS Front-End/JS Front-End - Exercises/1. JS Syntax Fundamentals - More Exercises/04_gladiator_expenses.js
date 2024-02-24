function gladiatorExpensesTotal(lostFights, helmetPrice, swordPrice, shieldPrice, armorPrice) {
    let helmets = 0
    let swords = 0
    let shields = 0
    let armors = 0

    for (let i = 1; i < lostFights + 1; i++) {

        if (i % 2 === 0 && i % 3 === 0) {
            shields += 1

            if (shields % 2 === 0) {
                armors += 1
            }
        }

        if (i % 2 === 0) {
            helmets += 1
        }

        if (i % 3 === 0) {
            swords += 1
        }
    }

    let totalPrices = helmets * helmetPrice + swords * swordPrice + shields * shieldPrice + armors * armorPrice
    console.log(`Gladiator expenses: ${totalPrices.toFixed(2)} aureus`)
}
