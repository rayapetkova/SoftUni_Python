function catConstructor(cats) {
    class Cat {
        constructor(name, age) {
            this.name = name
            this.age = age
        }

        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`)
        }
    }

    for (let cat of cats) {
        let [catName, catAge] = cat.split(' ')
        let catFromClass = new Cat(catName, catAge)
        catFromClass.meow()
    }
}
