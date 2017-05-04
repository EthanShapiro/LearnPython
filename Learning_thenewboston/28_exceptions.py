while True:
    try:
        number = int(input("Whats your favorite number?"))
        print(18/number)
        break
    except ValueError:
        print("Please input a number")
    except ZeroDivisionError:
        print("You cannot divide by 0")
    except:
        break
    finally:
        print("banana")
