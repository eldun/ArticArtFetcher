import tkinter as tk
import model, view, controller

if __name__ == "__main__":
    # Create window
    window = tk.Tk()
    window.title("ArticArtFetcher")
    window.columnconfigure(index=0, weight=1)
    window.rowconfigure(index=0, weight=1)
    window.minsize(800,400)

    # Create frame for window
    main_application = view.MainApplication(parent=window)
    main_application.grid(column=0, row=0, sticky=(tk.NSEW))

    # Configure resize
    main_application.columnconfigure(index=0, weight=1)
    main_application.columnconfigure(index=1, weight=1)
    # Log pane should be the only row that shrinks/resizes
    main_application.rowconfigure(index=1, weight=1)

    model = model.Model()
    view = main_application
    controller = controller.Controller(model, view)

    view.set_controller(controller)
    view.configure_bindings()

    window.mainloop()




